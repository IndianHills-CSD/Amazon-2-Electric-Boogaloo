CREATE TABLE [dbo].[Users]
(
	[EmailID] VARCHAR(50) NOT NULL PRIMARY KEY,
    [UserName] VARCHAR(50) NOT NULL,
    [Password] VARCHAR(50) NOT NULL
)

CREATE TABLE [dbo].[Post] (
    [PostID]   INT             NOT NULL,
    [Author]   VARCHAR (50)    NOT NULL,
    [Title]    VARCHAR (20)    NOT NULL,
    [Desc]     VARCHAR (100)    NOT NULL,
    [Location] VARCHAR (50)    NOT NULL,
    [Price]    DECIMAL (20, 2) NOT NULL,
    PRIMARY KEY CLUSTERED ([PostID] ASC)
)

INSERT INTO Users
VALUES
('kylervanderaa@gmail.com','KylerVan','password123!');
INSERT INTO Users
VALUES
('Amazon2Admin@email.net','AdminAccount','AdminPassword');

INSERT INTO Post
VALUES
(1,'KylerVan','Selling Laptop', 'I am selling a very cool laptop that comes with built in keyboard and half a screen', 'Ottumwa, IA', 19.99);

INSERT INTO Post
VALUES
(2,'KylerVan','Selling Books', 'Class Books For Sale', 'Macon, MO', 10000.33);

INSERT INTO Post
VALUES
(3,'AdminAccount','Trading Notes', 'I would like to trade my notes for X class for notes from Y class', 'Des Moines, IA', 1.00);

INSERT INTO Post
VALUES
(4,'AdminAccount','Selling Sandwhich', 'Selling a lightly used sandwhich. Entertaining all offers.', 'Ottumwa, IA', 10.00);