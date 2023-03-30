export interface IRepository<T>{
    getAll(filter: any|undefined):Promise<T[] | null>;
    get(id: string|number): Promise<T | null>;
    create(entity: T): Promise<void>;
    update(entity: Partial<T>): Promise<void>;
    delete(id: string|number): Promise<void>;
}
