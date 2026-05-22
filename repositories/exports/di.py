from fastapi import Depends
from db.connection import get_db
from repositories.exports.factory import RepositoryFactory

def get_user_repository(
    db = Depends(get_db)
):
    return RepositoryFactory.create_user_repository(db)

def get_book_repository(
    db = Depends(get_db)
):
    return RepositoryFactory.create_book_repository(db)

def get_book_copy_repository(
    db = Depends(get_db)
):
    return RepositoryFactory.create_book_copy_repository(db)

def get_loan_repository(
    db = Depends(get_db)
):
    return RepositoryFactory.create_loan_repository(db)
