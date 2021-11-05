CREATE TABLE document (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"text" TEXT NOT NULL
);

CREATE TABLE summary (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	document_id INTEGER NOT NULL,
	summary TEXT NOT NULL,
	CONSTRAINT summary_FK FOREIGN KEY (document_id) REFERENCES document(id)
);
