import { it, expect, afterEach, beforeEach, test, describe } from 'vitest';
import WS from 'vitest-websocket-mock';
import { add, fetchDog } from './fortest';

let server: WS;
let client: WebSocket;

beforeEach(async () => {
  server = new WS('ws://localhost:1234');
  client = new WebSocket('ws://localhost:1234');
  await server.connected;
});

afterEach(() => {
  WS.clean();
});

describe('TEST ENVIRONMENT', () => {
  test('일반 함수 테스트', () => {
    const ret = add([1, 2, 3, 4, 5]);
    expect(ret).toBe(15);
  });
  test('async 함수 테스트', async () => {
    const status = await fetchDog();
    expect(status).toBe('success');
  });
});

describe('TEST ENVIRONMENT VIRTUAL WS SERVER', () => {
  test('connect 테스트', async () => {
    expect(client.readyState).toBe(WebSocket.OPEN);
  });
  test('send 테스트', async () => {
    client.send('hello, world!');
    await expect(server).toReceiveMessage('hello, world!');
    expect(server).toHaveReceivedMessages(['hello, world!']);
  });
  test('receive 테스트', async () => {
    const messages = { client: new Array() };
    client.onmessage = (e) => {
      messages.client.push(e.data);
    };
    client.send('hello, world!');
    server.send('hello, world!');
    expect(messages).toEqual({ client: ['hello, world!'] });
  });
  test('server close 테스트 with JSON', async () => {
    WS.clean();
    server = new WS('ws://localhost:1234', { jsonProtocol: true });
    client = new WebSocket('ws://localhost:1234');

    server.on('connection', (socket) => {
      socket.close({ wasClean: false, code: 1003, reason: '그 냥' });
    });
    client.onclose = (e: CloseEvent) => {
      expect(e.code).toBe(1003);
      expect(e.wasClean).toBe(false);
      expect(e.reason).toBe('그 냥');
    };
    await server.connected;
    await server.closed;
    expect(client.readyState).toBe(WebSocket.CLOSED);
  });
  test('server error 발생 테스트', async () => {
    WS.clean();
    server = new WS('ws://localhost:1234', { jsonProtocol: true });
    client = new WebSocket('ws://localhost:1234');
    await server.connected;
    const status: any = {
      disconnected: null,
      error: null,
    };
    client.onclose = (e) => {
      status.disconnected = true;
    };
    client.onerror = (e) => {
      status.error = e;
    };
    server.send('에러 받아라!');
    server.error();

    expect(status.disconnected).toBe(true);
    expect(status.error.origin).toBe('ws://localhost:1234/');
    expect(status.error.type).toBe('error');
    expect(client.readyState).toBe(WebSocket.CLOSED);
  });
  test('JSON send & receive 테스트', async () => {
    WS.clean();
    server = new WS('ws://localhost:1234', { jsonProtocol: true });
    client = new WebSocket('ws://localhost:1234');
    await server.connected;
    client.send(`{ "type": "아침인사", "payload": "하이요" }`);
    await expect(server).toReceiveMessage({
      type: '아침인사',
      payload: '하이요',
    });
    expect(server).toHaveReceivedMessages([
      { type: '아침인사', payload: '하이요' },
    ]);

    let message = null;
    client.onmessage = (e) => {
      message = e.data;
    };

    server.send({ type: '대답', payload: '방가방가' });
    expect(message).toEqual(`{"type":"대답","payload":"방가방가"}`);
  });
});

// describe('APIs', () => {
//   test('connect', async () => {
//     WS.clean();
//     server = new WS('ws://localhost:1234');
//     mySocketClass.connect('ws://localhost:1234');
//     await server.connected;
//     expect(mySocketClass.readyState).toBe(WebSocket.OPEN);
//   });
//   // test('응답 수신 테스트', async () => {});
// });
