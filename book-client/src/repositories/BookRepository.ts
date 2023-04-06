import Book from "../models/Book";
import { IRepository } from "./IRepository";
import config from "../config";
import axios from 'axios';

interface BookFilter {
    categoryId: string
  }
  

export class BookRepository implements IRepository<Book> {
    urlPrefix = config.remoteRepositoryUrlPrefix

    async getAll(filter: BookFilter): Promise<Book[] | null> {
      const params = { categoryId: filter.categoryId };
      let result;    
      if (params.categoryId) {
        result = await axios.get<Book[]>(`${this.urlPrefix}/book/`, { params });
      } else {
        result = await axios.get<Book[]>(`${this.urlPrefix}/book/`);
      }    
      return result.data
    }
    async get(id: number|string): Promise<Book | null>{
      const result = await axios.get<Book>(`${this.urlPrefix}/book/${id}`)    
      return result.data
    }
    async create(entity: Partial<Book>): Promise<void>{
      const result = await axios.post<Book>(`${this.urlPrefix}/book`, entity)
      console.log(result.data)
    }
    async update(entity: Partial<Book>): Promise<void>{
      const result = await axios.put<Book>(`${this.urlPrefix}/book/${entity.id}`, entity)
      console.log(result.data)
    }
    async delete(id: number|string): Promise<void>{
      const result = await axios.delete<Book>(`${this.urlPrefix}/book/${id}`)
      console.log(result.data)
    }
  
}
