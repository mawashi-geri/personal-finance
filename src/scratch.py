from typing import TypeVar, Generic

import pandas as pd
import polars as pl


T = TypeVar('T')


class Container(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value
    
    def get(self) -> T:
        return self.value
    
    def set(self, value: T) -> None:
        self.value = value


# Usage examples
int_container = Container[int](42)
print(int_container.get())

str_container = Container[str]("Hello")
print(str_container.get())


class PandasContainer(Container[pd.DataFrame ]):
    pass


class PolarsContainer(Container[pl.DataFrame ]):
    pass

class ContainerX(PolarsContainer):
    pass

polars_container = PolarsContainer(pl.DataFrame({"column1": [1, 2, 3], "column2": ["a", "b", "c"]}))
print(polars_container.get())

pandas_container = PandasContainer(pd.DataFrame({"column1": [4, 5, 6], "column2": ["d", "e", "f"]}))
print(pandas_container.get())


container_x = ContainerX(pl.DataFrame({"columnX": [7, 8, 9], "columnY": ["g", "h", "i"]}))
print(container_x.get())
