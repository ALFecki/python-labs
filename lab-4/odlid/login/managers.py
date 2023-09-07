from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(
        self, email, unique_code, phone, city, address, password, **extra_fields
    ):
        if not email:
            raise ValueError("Email must be set")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            unique_code=unique_code,
            phone=phone,
            city=city,
            address=address,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email="root@odlid.com",
        unique_code=0,
        phone="+375291111111",
        city="Minsk",
        address="Pushkina",
        **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(
            email, unique_code, phone, city, address, **extra_fields
        )
