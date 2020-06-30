CREATE TABLE contacts
(
    sno integer NOT NULL,
    name text COLLATE pg_catalog."default" NOT NULL,
    phone_num character varying(50) COLLATE pg_catalog."default" NOT NULL,
    msg text COLLATE pg_catalog."default" NOT NULL,
    date date DEFAULT CURRENT_DATE,
    email character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT contacts_pkey PRIMARY KEY (sno)
)