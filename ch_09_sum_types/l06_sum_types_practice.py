from enum import Enum
from functools import reduce


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


def get_csv_status(status, data):
    match status:
        case CSVExportStatus.PENDING:
            d = list(map(lambda v: list(map(lambda s: str(s), v)), data))
            return ("Pending...", d)
        case CSVExportStatus.PROCESSING:
            d = reduce(lambda i, j: f"{i}\n{','.join(j)}", data, "")[1:]
            # d = reduce(lambda i, j: f"{i}\n{','.join(j)}", data[1:], ",".join(data[0]))
            print("data is: ", data)
            # print("d is :", d)
            return ("Processing...", d)
        case CSVExportStatus.SUCCESS:
            return ("Success!", data)
        case CSVExportStatus.FAILURE:
            d = get_csv_status(CSVExportStatus.PENDING, data)[1]
            d = get_csv_status(CSVExportStatus.PROCESSING, d)[1]
            return ("Unknown error, retrying...", d)
        case _:
            raise Exception("unknown export status")
