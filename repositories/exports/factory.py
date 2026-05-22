from repositories.book_repository import BookRepository
from repositories.user_repository import UserRepository
from repositories.book_copy_repository import BookCopyRepository
from repositories.loan_repository import LoanRepository

class RepositoryFactory:
    @staticmethod
    def create_user_repository(db):
        return UserRepository(db)

    @staticmethod
    def create_book_repository(db):
        return BookRepository(db)

    @staticmethod
    def create_book_copy_repository(db):
        return BookCopyRepository(db)

    @staticmethod
    def create_loan_repository(db):
        return LoanRepository(db)