import  config  from "../config";
import { IRepository } from "./IRepository";
import category from "../models/Category";
import axios from 'axios'


export class CategoryRepository implements IRepository<category> {
    urlPrefix = config.remoteRepositoryUrlPrefix
    async getAll(): Promise<category[] | null> {
        const result = await axios.get<category[]>(`${this.urlPrefix}/category`)
        return result.data
    }
    async get(id: string | number): Promise<category | null> {
        const result = await axios.get<category>(`${this.urlPrefix}/category/${id}`)
        return result.data
    }
    async create(entity: category): Promise<void> {
        const result = await axios.post<category>(`${this.urlPrefix}/category/`,entity)
        console.log(result.data)
    }
    async update(entity: Partial<category>): Promise<void> {
        const result = await axios.put<category>(`${this.urlPrefix}/category/${entity.id}`,entity)
        console.log(result.data)
    }
    async delete(id: string | number): Promise<void> {
        const result = await axios.delete<category>(`${this.urlPrefix}/category/${id}`)
        console.log(result.data)

    }
}
