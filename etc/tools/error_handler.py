class AppError(BaseException):

    def __init__(self, msg: str):
        self.msg = msg

    def __repr__(self):
        return self.msg
