import mysql.connector
from mysql import connector
import datetime

class Dbconnect:
    def get_connected(self):
        try:
            self.connection = connector.connect(
                host = "localhost",
                user = "root",
                password = "Sana#2004",
                database = "library_db"
            )
            return self.connection
        except Exception as e:
            print(e)
            return None

class BookManager(Dbconnect):

    def post(self, **kwargs):
        try:
            self.connect = super().get_connected()

            if self.connect is None:
                return

            self.cursor = self.connect.cursor()

            query = """
            INSERT INTO book
            (title, author, category, price, published_date)
            VALUES (%s, %s, %s, %s, %s)
            """

            values = [v for v in kwargs.values()]

            self.cursor.execute(query, values)
            self.connect.commit()

            print("Book added successfully")

        except Exception as e:
            print(e)

    def get(self):
        try:
            self.connect = super().get_connected()

            if self.connect is None:
                return

            self.cursor = self.connect.cursor()

            query = "SELECT * FROM book"

            self.cursor.execute(query)

            records = self.cursor.fetchall()

            for record in records:
                print(record)

        except Exception as e:
            print(e)



    def get_object(self, id=None):
            try:
                self.connect = super().get_connected()

                if self.connect is None:
                    return None

                self.cursor = self.connect.cursor()

                query = "SELECT * FROM book WHERE id = %s"
                values = (id,)

                self.cursor.execute(query, values)

                record = self.cursor.fetchone()

                return record

            except Exception as e:
                print(e)
                return None

    def retrieve(self, id=None):
        try:
            self.connect = super().get_connected()

            if self.connect is None:
                return

            self.cursor = self.connect.cursor()

            query = "SELECT * FROM book WHERE id = %s"
            values = (id,)

            self.cursor.execute(query, values)

            record = self.cursor.fetchone()

            if record is not None:
                print(record)
            else:
                print("Book not found...")

        except Exception as e:
            print(e)

    def put(self, id=None, **kwargs):
        try:
            record = self.get_object(id=id)

            if record is not None:
                self.connect = super().get_connected()

                if self.connect is None:
                    return

                self.cursor = self.connect.cursor()

                placeholder = ", ".join(
                    [k + " = %s" for k in kwargs.keys()]
                )

                query = f"UPDATE book SET {placeholder} WHERE id = %s"

                values = list(kwargs.values())
                values.append(id)

                self.cursor.execute(query, values)
                self.connect.commit()

                print("Book details updated successfully...!!")

            else:
                print("Book not found. Details not updated...!!")

        except Exception as e:
            print(e)

    def delete(self, id=None):
        try:
            self.connect = super().get_connected()

            if self.connect is None:
                return

            self.cursor = self.connect.cursor()

            # Check whether book exists
            query = "SELECT * FROM book WHERE id = %s"
            values = (id,)

            self.cursor.execute(query, values)
            record = self.cursor.fetchone()

            if record is not None:

                query = "DELETE FROM book WHERE id = %s"

                self.cursor.execute(query, values)
                self.connect.commit()

                print("Book deleted successfully...!")

            else:
                print("Book not found...")

        except Exception as e:
            print(e)
book = BookManager()

# book.post(
#     title="Python Programming",
#     author="Sana Anwar",
#     category="Programming",
#     price=550.00,
#     published_date="2024-01-15"
# )
#
# book.post(
#     title="Database Systems",
#     author="Hana Anwar",
#     category="Database",
#     price=650.00,
#     published_date="2023-06-20"
# )
#
# book.post(
#     title="Machine Learning",
#     author="Anjana Krishna",
#     category="AI",
#     price=750.00,
#     published_date="2025-02-10"
# )
#
# book.post(
#     title="Data Science",
#     author="Rithu Marry",
#     category="Data Science",
#     price=600.00,
#     published_date="2024-08-12"
# )

print("___________get________________________")
book.get()

print("----------------retrieve----------------")
book.retrieve(1)

print("----------put/update---------------")
book.put(1, title="Python Full Stack Development")
print("___________get________________________")
book.get()

print("------------delete-------------")
book.delete(3)
print("___________get________________________")
book.get()

