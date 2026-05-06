from core.security import verify_password, generate_token, hash_password
from api.dtos.login_dto import RegisterUserDto
from domain.user import User, UserCredentials
from repositories.user_repository import UserRepository

class AuthService:
    def __init__(
            self,
            user_repo : UserRepository
        ) -> None:
        self.user_repo = user_repo


    async def validateUser(
            self,
            email : str,
            password : str
        ) -> str | None:
        user = self.user_repo.getUserCredentials(email)
        print(user)
        if (user is not None) and verify_password(password,user.credentials.password_hash) :
            token = generate_token(str(user.email),user.role)
            return token
        return None

    async def registerUser(self, userDto : RegisterUserDto):
        userDto.password = hash_password(password=userDto.password)
        try:
            self.user_repo.saveUserLector(User(
                uid="",
                full_name=userDto.fullname,
                email=userDto.email,
                contact_number=userDto.contact_number,
                role="lector",
                credentials=UserCredentials(
                    password_hash=userDto.password
                )
            ))
            return True
        except Exception as e:
            print(e)
            return False