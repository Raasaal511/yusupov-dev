from infrastructure.repositories.content import CategoryRepository


class CategoryUnitOfWork:
    def __init__(self, session):
        self.session = self.session
        self.repo = CategoryRepository(session=session)

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
