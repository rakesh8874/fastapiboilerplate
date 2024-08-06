from sqlalchemy.orm import Session
from typing import Type, TypeVar, List, Optional

T = TypeVar("T")


class DataProcessor:
    def __init__(self, model: Type[T], session: Session):
        self.model = model
        self.session = session

    def filter_data(self, query, **filters):
        for key, value in filters.items():
            if value is not None:
                query = query.filter(getattr(self.model, key) == value)
        return query

    def paginate_data(self, query, page: int, page_size: int):
        return query.offset((page - 1) * page_size).limit(page_size)

    def sort_data(self, query, by: str, ascending: bool):
        if by:
            if ascending:
                query = query.order_by(getattr(self.model, by).asc())
            else:
                query = query.order_by(getattr(self.model, by).desc())
        return query

    def search_data(self, query, column: str, keyword: str):
        if column and keyword:
            query = query.filter(getattr(self.model, column).ilike(f"%{keyword}%"))
        return query

    def process_data(self, filters: dict = {}, page: Optional[int] = None, page_size: Optional[int] = None,
                     by: Optional[str] = None, ascending: Optional[bool] = True, column: Optional[str] = None,
                     keyword: Optional[str] = None):
        query = self.session.query(self.model)
        query = self.filter_data(query, **filters)
        query = self.search_data(query, column, keyword)
        query = self.sort_data(query, by, ascending)
        if page and page_size:
            query = self.paginate_data(query, page, page_size)
        return query.all()
