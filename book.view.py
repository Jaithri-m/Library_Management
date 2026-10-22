from mysql import connector

class Dbconnect:
    def get_connection(self):
        try:
            self.connection = connector.connect(
                host="localhost",
                user="root",
                password="JAITHRIm2005@7736",
                database="book_db"
            )
            return self.connection

        except Exception as e:
            print(e)
            return None


class LibraryManager(Dbconnect):

    def get(self):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()

            query = "SELECT * FROM book_details"
            self.cursor.execute(query)

            records = self.cursor.fetchall()
            return records

        except Exception as e:
            print(e)
            return []

        finally:
            if hasattr(self, "cursor"):
                self.cursor.close()
            if hasattr(self, "connect") and self.connect:
                self.connect.close()

    def post(self, **kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()

            query = """
                INSERT INTO book_details
                (book_name, author_name, price, type, published_year)
                VALUES (%s, %s, %s, %s, %s)
            """

            values = (kwargs["book_name"],kwargs["author_name"],kwargs["price"],kwargs["type"],kwargs["published_year"])

            self.cursor.execute(query, values)
            self.connect.commit()

            print("New book added successfully...!")

        except Exception as e:
            print(e)

        finally:
            if hasattr(self, "cursor"):
                self.cursor.close()
            if hasattr(self, "connect") and self.connect:
                self.connect.close()

    def get_object(self, id=None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()

            query = "SELECT * FROM book_details WHERE id = %s"
            values = (id,)

            self.cursor.execute(query, values)
            record = self.cursor.fetchone()

            return record

        except Exception as e:
            print(e)
            return None

        finally:
            if hasattr(self, "cursor"):
                self.cursor.close()
            if hasattr(self, "connect") and self.connect:
                self.connect.close()

    def retrieve(self, id=None):
        record = self.get_object(id=id)

        if record is not None:
            print(record)
        else:
            print("Book not found...!")

    def delete(self, id=None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()

            query = "DELETE FROM book_details WHERE id = %s"
            values = (id,)

            self.cursor.execute(query, values)
            self.connect.commit()

            if self.cursor.rowcount > 0:
                print("Book deleted successfully...!")
            else:
                print("Book not found...!")

        except Exception as e:
            print(e)

        finally:
            if hasattr(self, "cursor"):
                self.cursor.close()
            if hasattr(self, "connect") and self.connect:
                self.connect.close()

    def put(self, id=None, **kwargs):
        try:
            allowed_fields = [
                "book_name", "author_name", "price",
                "type", "published_year"
            ]

            if not kwargs or not all(k in allowed_fields for k in kwargs):
                print("Invalid or empty update data...!")
                return

            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()

            placeholder = ""

            for k in kwargs.keys():
                placeholder += k + " = %s, "

            placeholder = placeholder.rstrip(", ")

            query = (
                f"UPDATE book_details SET {placeholder} "
                "WHERE id = %s"
            )

            values = list(kwargs.values())
            values.append(id)

            self.cursor.execute(query, values)
            self.connect.commit()

            if self.cursor.rowcount > 0:
                print("Book updated successfully...!")
            else:
                print("Book not found or no changes made...!")

        except Exception as e:
            print(e)

        finally:
            if hasattr(self, "cursor"):
                self.cursor.close()
            if hasattr(self, "connect") and self.connect:
                self.connect.close()





# book_instance = LibraryManager()

# book_instance.get()

# book_instance.post(book_name="The Shining",author_name="Stephen King",price=450,type="Horror",published_year=1977)
# book_instance.post(book_name="Wings of Fire",author_name="A. P. J. Abdul Kalam",price=350,type="Biography",published_year=1999)
# book_instance.post(book_name="Harry Potter",author_name="J. K. Rowling",price=500,type="Fantasy",published_year=1997)
# book_instance.post(book_name="The Shining", author_name="Stephen King",price=450, type="Horror", published_year=1977)

# book_instance.retrieve(id=1)

# book_instance.delete(id=1)

# book_instance.put(id=1, price=500, type="Thriller")
