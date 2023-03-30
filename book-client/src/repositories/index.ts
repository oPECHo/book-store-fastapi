import { BookRepository } from "./BookRepository"
import { CategoryRepository } from "./CategoryRepository"

const repositories = {
  books: new BookRepository(),
  categories: new CategoryRepository(),
}

export default repositories
