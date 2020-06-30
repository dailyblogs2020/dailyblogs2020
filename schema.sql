CREATE TABLE posts
(
    sno integer NOT NULL,
    title text COLLATE pg_catalog."default" NOT NULL,
    tagline text COLLATE pg_catalog."default" NOT NULL,
    slug character varying(50) COLLATE pg_catalog."default" NOT NULL,
    content text COLLATE pg_catalog."default" NOT NULL,
    img_file character varying(50) COLLATE pg_catalog."default" NOT NULL,
    credit text COLLATE pg_catalog."default" NOT NULL,
    post_img character varying(50) COLLATE pg_catalog."default" NOT NULL,
    date date DEFAULT CURRENT_DATE,
    CONSTRAINT posts_pkey PRIMARY KEY (sno)
)
