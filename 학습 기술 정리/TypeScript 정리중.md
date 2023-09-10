# TypeScript 정리

학습 후기 : **사실 처음에는 많이들 쓰고, 타입에 엄격해서 사용했음. 실제로 디버그나 스니펫 등 다양한 부분에서 도움이 된다고 생각했지만... JS의 유연함과 TS의 엄격함 서로 차이가 있는데, 어떤 라이브러리를 배울 때 TS로 배운 뒤 JS DOCS로 돌아가면 좋을 것 같다. 사실 TS만의 압도적인 장점을 느끼진 못했음.**

- 핸드북 존재 `https://typescript-kr.github.io/`

## WHY?

- 우선적으로 사용하며 깨달은 사용 이유에 대해 작성하겠음.

### 1. 남이 짠 라이브러리와 코드에 대한 파악이 쉬워진다.

- 커서를 올리고 기다리는 것으로, 라이브러리의 기능에 대해 짐작을 할 수 있음.
- 왜냐? 일반적으로 react의 경우, hook을 통해 기능을 묶어두고 Component로 기능을 구현하는 형태인데 TypeScript의 경우 그 자리에서 return 값들과 params 값들을 확인 할 수 있다.
- 즉, 이름을 고민하고 고민해서 잘 지어서 라이브러리로 만드는 것이기에, 이름만 보고도 짐작이 가능하다. 특히, 어떤 인자를 받아서 어떤 값을 리턴한다! 라는 내용을 알 수 있기에, 그렇다면 이 값을 통해 이런 값을 추출하고 이런 행동을 하겠구나! 라고 예측을 하고 코드를 칠 수 있어서, 코드를 짤 때 이해도가 더 높아짐.
- 당장 예시를 들자면 React-Hook-Form의 경우, 시작부터 TS로 시작하였는데, useFieldArray 혹은 Controller 등의 사용법을 독스와 함께 해당 함수가 받는 인자, 반환값 등을 통해 기능을 명확히 알 수 있다.
- 아마 이 강점때문에, 나는 쭉 타입스크립트를 사용 할 듯 하다. TS와 JS DOC을 함께 사용할 경우 가독성이 매우 높아질 것으로 예상되고, 실제로 나도 각종 라이브러리에서 그런 형태로 작성해주었기에 이해가 빨라진 것이다.

### 2. 자동완성 되고, Compile 단에서, IDE 단에서 디버깅이 가능하다.

- 이건 그냥 쓰니 자동으로 되서 좋다. 딱 타입 선언의 불편함만큼 편해진다.
- 컴파일 단계에서 `undefined`나 유니온 타입 등 다양한 예외 상황에 대해 분기처리가 가능하며, 타입에 따라 분기처리가 가능하기에 하나의 함수에 대해 `try-catch`를 하나 줄일 수 있는 것 같다.

## WHAT?

## HOW?

## WHAT IF?

## 추후 정리 예정

1. unknown & any
   - [unknown 관련 글](https://jbee.io/typescript/TS-9-unknown/)
   - [안전한 any 만들기](https://overcurried.netlify.app/%EC%95%88%EC%A0%84%ED%95%9C%20any%20%ED%83%80%EC%9E%85%20%EB%A7%8C%EB%93%A4%EA%B8%B0/)

### enum 관련 정리

- 타입스크립트 참고할만한 글 : https://kschoi.github.io/typescript/typescript/

TS에서의 튜플 타입 : 그냥 간단히 말해서 배열인데 내부에 타입이 상세하게 선언된 것.
TS에서의 enum 타입 : 조금 신기하게 생겼는데 어떻게 써야하나 잘 모르겠음. 아래와 같이 사용함.

```js
enum Team {
  Manager,
  Planner,
  Developer,
  Designer
}
// 위와 같이 선언하면 자동으로 배열처럼 0,1,2,3이 할당된다.
enum Team {
  Manager = 123,
  Planner = 321,
  Developer = 404,
  Designer // 405 자동 할당
}
// 위와 같이 지정해서 선언하면 값이 할당된다.
```

enum 값은 Team.Manager로 123을 호출 할 수 있으며, Team[123]으로 "Manager"를 호출 할 수 있다.
또한, 숫자가 아닌 문자도 할당이 가능한 것으로 보인다.

### union type

유니온 타입의 경우 그냥 string | number 이런 식으로 union 해주는 것.

함수 리턴 타입 : 함수에서 그냥 선언해도 되고, type으로 만들어서 선언해도 되고, interface로 선언해서 사용해도 된다.

인터페이스는 인터페이스 상속 가능.
type으로 선언하는 타입 얼라이어스(앨리어스 alias)는 원시값, 유니온 타입, 튜플 등도 타입으로 지정이 가능하다. 직접 값을 지정 할 수 있다는 것은 좋은거야~

```js
// 문자열 리터럴로 타입 지정
type Str = 'Lee';

// 유니온 타입으로 타입 지정
type Union = string | null;

// 문자열 유니온 타입으로 타입 지정
type Name = 'Lee' | 'Kim';

// 숫자 리터럴 유니온 타입으로 타입 지정
type Num = 1 | 2 | 3 | 4 | 5;

// 객체 리터럴 유니온 타입으로 타입 지정
type Obj = { a: 1 } | { b: 2 };

// 함수 유니온 타입으로 타입 지정
type Func = (() => string) | (() => void);

// 인터페이스 유니온 타입으로 타입 지정
type Shape = Square | Rectangle | Circle;

// 튜플로 타입 지정
type Tuple = [string, boolean];
const t: Tuple = ['', '']; // Error
```

## 제네릭

- 주로 한 가지 타입보다 여러가지 타입에서 동작하는 컴포넌트를 생성하는데 사용된다.
- `<T>` 로 받아서 사용

## 고쳐야 할 점

1. 타입과 인터페이스를 모아서 관리하지 못했다.
2. 해당 부분에서도 참고 할 것들이 많으면 좋겠다.

## TypeScript config file 관리

```js
{
  "compilerOptions": {
    /* Visit https://aka.ms/tsconfig.json to read more about this file */

    /* Projects */
    // "incremental": true,                              /* Enable incremental compilation */
    // "composite": true,                                /* Enable constraints that allow a TypeScript project to be used with project references. */
    // "tsBuildInfoFile": "./",                          /* Specify the folder for .tsbuildinfo incremental compilation files. */
    // "disableSourceOfProjectReferenceRedirect": true,  /* Disable preferring source files instead of declaration files when referencing composite projects */
    // "disableSolutionSearching": true,                 /* Opt a project out of multi-project reference checking when editing. */
    // "disableReferencedProjectLoad": true,             /* Reduce the number of projects loaded automatically by TypeScript. */

    /* Language and Environment */
    "target": "esnext" /* Set the JavaScript language version for emitted JavaScript and include compatible library declarations. */,
    "lib": [
      "dom",
      "esnext"
    ] /* Specify a set of bundled library declaration files that describe the target runtime environment. */,
    "jsx": "react" /* Specify what JSX code is generated. */,
    // "experimentalDecorators": true,                   /* Enable experimental support for TC39 stage 2 draft decorators. */
    // "emitDecoratorMetadata": true,                    /* Emit design-type metadata for decorated declarations in source files. */
    // "jsxFactory": "",                                 /* Specify the JSX factory function used when targeting React JSX emit, e.g. 'React.createElement' or 'h' */
    // "jsxFragmentFactory": "",                         /* Specify the JSX Fragment reference used for fragments when targeting React JSX emit e.g. 'React.Fragment' or 'Fragment'. */
    // "jsxImportSource": "",                            /* Specify module specifier used to import the JSX factory functions when using `jsx: react-jsx*`.` */
    // "reactNamespace": "",                             /* Specify the object invoked for `createElement`. This only applies when targeting `react` JSX emit. */
    // "noLib": true,                                    /* Disable including any library files, including the default lib.d.ts. */
    // "useDefineForClassFields": true,                  /* Emit ECMAScript-standard-compliant class fields. */

    /* Modules */
    "module": "esnext" /* Specify what module code is generated. */,
    // "rootDir": "./",                                  /* Specify the root folder within your source files. */
    "moduleResolution": "node" /* Specify how TypeScript looks up a file from a given module specifier. */,
    "baseUrl": "src" /* Specify the base directory to resolve non-relative module names. */,
    "paths": {
      "@assets/*": ["assets/*"],
      "@components/*": ["components/*"],
      "@contexts/*": ["contexts/*"],
      "@hooks/*": ["hooks/*"],
      "@layouts/*": ["layouts/*"],
      "@pages/*": ["pages/*"],
      "@queries/*": ["queries/*"],
      "@styles/*": ["styles/*"],
      "@templates/*": ["templates/*"],
      "@utils/*": ["utils/*"]
    } /* Specify a set of entries that re-map imports to additional lookup locations. */,
    // "rootDirs": [],                                   /* Allow multiple folders to be treated as one when resolving modules. */
    // "typeRoots": [],                                  /* Specify multiple folders that act like `./node_modules/@types`. */
    // "types": [],                                      /* Specify type package names to be included without being referenced in a source file. */
    // "allowUmdGlobalAccess": true,                     /* Allow accessing UMD globals from modules. */
    // "resolveJsonModule": true,                        /* Enable importing .json files */
    // "noResolve": true,                                /* Disallow `import`s, `require`s or `<reference>`s from expanding the number of files TypeScript should add to a project. */

    /* JavaScript Support */
    // "allowJs": true,                                  /* Allow JavaScript files to be a part of your program. Use the `checkJS` option to get errors from these files. */
    // "checkJs": true,                                  /* Enable error reporting in type-checked JavaScript files. */
    // "maxNodeModuleJsDepth": 1,                        /* Specify the maximum folder depth used for checking JavaScript files from `node_modules`. Only applicable with `allowJs`. */

    /* Emit */
    // "declaration": true,                              /* Generate .d.ts files from TypeScript and JavaScript files in your project. */
    // "declarationMap": true,                           /* Create sourcemaps for d.ts files. */
    // "emitDeclarationOnly": true,                      /* Only output d.ts files and not JavaScript files. */
    // "sourceMap": true,                                /* Create source map files for emitted JavaScript files. */
    // "outFile": "./",                                  /* Specify a file that bundles all outputs into one JavaScript file. If `declaration` is true, also designates a file that bundles all .d.ts output. */
    // "outDir": "./",                                   /* Specify an output folder for all emitted files. */
    // "removeComments": true,                           /* Disable emitting comments. */
    // "noEmit": true,                                   /* Disable emitting files from a compilation. */
    // "importHelpers": true,                            /* Allow importing helper functions from tslib once per project, instead of including them per-file. */
    // "importsNotUsedAsValues": "remove",               /* Specify emit/checking behavior for imports that are only used for types */
    // "downlevelIteration": true,                       /* Emit more compliant, but verbose and less performant JavaScript for iteration. */
    // "sourceRoot": "",                                 /* Specify the root path for debuggers to find the reference source code. */
    // "mapRoot": "",                                    /* Specify the location where debugger should locate map files instead of generated locations. */
    // "inlineSourceMap": true,                          /* Include sourcemap files inside the emitted JavaScript. */
    // "inlineSources": true,                            /* Include source code in the sourcemaps inside the emitted JavaScript. */
    // "emitBOM": true,                                  /* Emit a UTF-8 Byte Order Mark (BOM) in the beginning of output files. */
    // "newLine": "crlf",                                /* Set the newline character for emitting files. */
    // "stripInternal": true,                            /* Disable emitting declarations that have `@internal` in their JSDoc comments. */
    // "noEmitHelpers": true,                            /* Disable generating custom helper functions like `__extends` in compiled output. */
    // "noEmitOnError": true,                            /* Disable emitting files if any type checking errors are reported. */
    // "preserveConstEnums": true,                       /* Disable erasing `const enum` declarations in generated code. */
    // "declarationDir": "./",                           /* Specify the output directory for generated declaration files. */
    // "preserveValueImports": true,                     /* Preserve unused imported values in the JavaScript output that would otherwise be removed. */

    /* Interop Constraints */
    // "isolatedModules": true,                          /* Ensure that each file can be safely transpiled without relying on other imports. */
    // "allowSyntheticDefaultImports": true,             /* Allow 'import x from y' when a module doesn't have a default export. */
    "esModuleInterop": true /* Emit additional JavaScript to ease support for importing CommonJS modules. This enables `allowSyntheticDefaultImports` for type compatibility. */,
    // "preserveSymlinks": true,                         /* Disable resolving symlinks to their realpath. This correlates to the same flag in node. */
    "forceConsistentCasingInFileNames": true /* Ensure that casing is correct in imports. */,

    /* Type Checking */
    "strict": true /* Enable all strict type-checking options. */,
    // "noImplicitAny": true,                            /* Enable error reporting for expressions and declarations with an implied `any` type.. */
    // "strictNullChecks": true,                         /* When type checking, take into account `null` and `undefined`. */
    // "strictFunctionTypes": true,                      /* When assigning functions, check to ensure parameters and the return values are subtype-compatible. */
    // "strictBindCallApply": true,                      /* Check that the arguments for `bind`, `call`, and `apply` methods match the original function. */
    // "strictPropertyInitialization": true,             /* Check for class properties that are declared but not set in the constructor. */
    // "noImplicitThis": true,                           /* Enable error reporting when `this` is given the type `any`. */
    // "useUnknownInCatchVariables": true,               /* Type catch clause variables as 'unknown' instead of 'any'. */
    // "alwaysStrict": true,                             /* Ensure 'use strict' is always emitted. */
    // "noUnusedLocals": true,                           /* Enable error reporting when a local variables aren't read. */
    // "noUnusedParameters": true,                       /* Raise an error when a function parameter isn't read */
    // "exactOptionalPropertyTypes": true,               /* Interpret optional property types as written, rather than adding 'undefined'. */
    // "noImplicitReturns": true,                        /* Enable error reporting for codepaths that do not explicitly return in a function. */
    // "noFallthroughCasesInSwitch": true,               /* Enable error reporting for fallthrough cases in switch statements. */
    // "noUncheckedIndexedAccess": true,                 /* Include 'undefined' in index signature results */
    // "noImplicitOverride": true,                       /* Ensure overriding members in derived classes are marked with an override modifier. */
    // "noPropertyAccessFromIndexSignature": true,       /* Enforces using indexed accessors for keys declared using an indexed type */
    // "allowUnusedLabels": true,                        /* Disable error reporting for unused labels. */
    // "allowUnreachableCode": true,                     /* Disable error reporting for unreachable code. */

    /* Completeness */
    // "skipDefaultLibCheck": true,                      /* Skip type checking .d.ts files that are included with TypeScript. */
    "skipLibCheck": true /* Skip type checking all .d.ts files. */
  },
  "include": [
    "./src/**/*",
    "./gatsby-node.ts",
    "./gatsby-config.ts",
    "./plugins/**/*"
  ]
}
```

---

## 참고 문헌들

- 주로 타입스크립트 공식 독스와 구글링 상단 게시글임.
- https://www.typescriptlang.org/docs/handbook/type-compatibility.html#private-and-protected-members-in-classes
- https://www.typescriptlang.org/docs/handbook/2/objects.html#interfaces-vs-intersections

### enum type

- 아래와 같이 지정하고 사용

```js
export enum Test {
  Hi = '1',
  Hello = '2',
  Lego = '3'
}

console.log(Test.Hi) // 1
console.log(Test.Hello) // 2
console.log(Test.Lego) // 3
```

### intersection types

- 간단히 말해서, `&` 연산자로 새로 생성되는 type이다.

```js
interface AType {
  test1: number;
}
interface BType {
  test2: number;
}
type ABType = Atype & BType;
```

### class 형태의 private 변수 관련

- `class`의 `implements`.

  1. `implements`는 `class`의 구조를 잡아주는 것이 아니다.
  2. `implements`는 `class`가 `implements`된 `interface`의 값을 가지고 있는지 검증하는 용도이다.

- `getter`, `setter` 관련

  0. `getter`와 `setter`를 사용하는 이유는 객체 내부 속성의 직접 접근을 막아 보안을 강화하고, 코드 안정성과 유지보수성을 늘릴 수 있다.
  1. class에 `get test() {return 'test'}`라는 `getter`가 선언되어 있다면, 해당 값은 `interface`에서는 `get test(): string;` 형태로 선언한다.
  2. `setter`는 `return type`이 없다. 즉, `interface`로 `setter`를 검증하고 싶다면 `set setDate(newDate: string)` 이런 형태로 선언하면 된다.
  3. `setter`를 선언 할 때 주의점으로는 `args` 즉 인자를 하나만 받을 수 있다는 것이다.
  4. `getter`는 그냥 변수 쓰듯 쓰면 된다. `SomeClass.test` 이런 형태로.

  - 참고해보면 좋을 글 : https://lovethefeel.tistory.com/173

- `private` 검증(`implements`) 관련

  1. `private`은 `protected`를 선언한 타입과 유사하다. 하지만, 자식 클래스에서도 `private`을 지키는 점이 다르다. (docs에서는 `subclasses`에서도 access가 불가능하다고 설명.)
  2. `private`변수는 검증하면 안된다. 과거 버전에 명확히 적혀있던 규칙. 현재 독스에는 명확히 적혀있지 않고 약간 추상적으로 적혀있지만 통용되는 내용임.

### 제네릭

- 참고 : https://www.typescriptlang.org/docs/handbook/2/mapped-types.html
- 참고2 : https://inpa.tistory.com/entry/TS-%F0%9F%93%98-%ED%83%80%EC%9E%85%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-Generic-%ED%83%80%EC%9E%85-%EC%A0%95%EB%B3%B5%ED%95%98%EA%B8%B0
- 참고3 : https://www.tutorialsteacher.com/typescript/typescript-generic-interface
- 참고4 : https://hyunseob.github.io/2017/01/14/typescript-generic/
- 참고5 : https://stackoverflow.com/questions/62233382/how-do-i-define-and-call-a-generic-function-parameter-in-typescript

- 아래는 객체 나름 재밌는 제네릭인듯? 자동 제네릭 같음

```js
type MappedType<T> = {
  [Properties in keyof T]: T[Properties];
};

interface DefaultData<DataType, StoreType, SourceType> {
  data: MappedType<DataType>;
  stores: MappedType<StoreType>;
  source: MappedType<SourceType>;
}
```
