class Admin:
    def __init__(self,user_id,username,password_harsh):
        super().__init__(
            user_id = user_id,
            username = username,
            password_harsh = password_harsh,
            role = "admin"

        )