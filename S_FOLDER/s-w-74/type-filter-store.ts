import { makeAutoObservable } from 'mobx';
import { useState } from 'react';

export class TypeController {
  private __typeFilterSet: Set<number>;

  constructor() {
    this.__typeFilterSet = new Set();
    makeAutoObservable(this);
  }

  get TypeIdFilterSet() {
    return this.__typeFilterSet;
  }

  updateTypeIdFilterSet(typeIdFilter: Set<number>) {
    this.__typeFilterSet = typeIdFilter;
  }
}

export const useTypeFilter = function () {
  const [typeController, _] = useState<TypeController>(new TypeController());
  return { typeController };
};
