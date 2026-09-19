# Template Method: the base class owns the algorithm skeleton.
# Subclasses fill in the varying steps — they do not rewrite the sequence.

from abc import ABC, abstractmethod


# ----------- Abstract Class (template) -----------
class AbstractReportExporter(ABC):
    def export_report(self, data, path):
        rows = self.prepare_data(data)
        self.open_file(path)
        self.write_header(rows)
        self.write_data_rows(rows)
        self.write_footer(rows)
        self.close_file(path)
        print(f"Report exported to {path}")

    def prepare_data(self, data):
        print(f"Preparing data: {data}")
        return sorted(data, key=lambda x: x.get("name"))

    def open_file(self, path):
        print(f"Opening file: {path}")

    def close_file(self, path):
        print(f"Closing file: {path}")

    @abstractmethod
    def write_header(self, rows):
        pass

    @abstractmethod
    def write_data_rows(self, rows):
        pass

    @abstractmethod
    def write_footer(self, rows):
        pass


# ----------- Concrete Classes -----------
class CSVReportExporter(AbstractReportExporter):
    def write_header(self, rows):
        print("CSV Header: name, age, city")

    def write_data_rows(self, rows):
        for row in rows:
            print(f'CSV Row: {row["name"]}, {row["age"]}, {row["city"]}')

    def write_footer(self, rows):
        print(f"CSV Footer: {len(rows)} rows")


class JSONReportExporter(AbstractReportExporter):
    def write_header(self, rows):
        print("[")

    def write_data_rows(self, rows):
        for i, row in enumerate(rows):
            comma = "," if i < len(rows) - 1 else ""
            print(f'  {{"name": "{row["name"]}", "age": {row["age"]}, "city": "{row["city"]}"}}{comma}')

    def write_footer(self, rows):
        print("]")


# ----------- Client Code -----------
def main():
    data = [
        {"name": "John", "age": 30, "city": "New York"},
        {"name": "Jane", "age": 25, "city": "Los Angeles"},
        {"name": "Jim", "age": 35, "city": "Chicago"},
    ]

    csv_exporter = CSVReportExporter()
    json_exporter = JSONReportExporter()

    csv_exporter.export_report(data, "report.csv")
    json_exporter.export_report(data, "report.json")


if __name__ == "__main__":
    main()
