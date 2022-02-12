from Table import Table

class TicketTable(Table):

    def __init__(self) -> None:
        super().__init__("ticket")
    

    def exists(self, code, db_connection):
        """
        Arguments: 
            id: ticket code (primary key)
            db_connection: psycopg2 db connection instance
        """
        #create a cursor
        cursor = db_connection.cursor()
        #execute query
        cursor.execute("SELECT * from {self.table_name} where code = '{code}'")
        #get selected records
        data = cursor.fetchall()
        #close cursor
        cursor.close()

        if data == []:
            return False
        
        return True