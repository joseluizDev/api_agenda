from enum import Enum


class CargoEnum(Enum):
    ADMIN = 1, 'admin'
    GERENTE = 2, 'gerente'
    FUNCIONARIO = 3, 'funcionario'
    ATENDENTE = 4, 'atendente'

    def __new__(cls, num, desc):
        obj = object.__new__(cls)
        obj._value_ = num
        obj.desc = desc
        return obj

    def __str__(self):
        return f'{self.desc}'

    @classmethod
    def get_enum(cls, num):
        """Retorna o Cargo correspondente ao número fornecido."""
        for cargo in cls:
            if cargo.value == num:
                return cargo
        raise ValueError(f'Cargo com número {num} não encontrado.')
