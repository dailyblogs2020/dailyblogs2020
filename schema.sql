--CREATE SEQUENCE posts_sno_seq;
CREATE TABLE posts
(
    sno integer NOT NULL DEFAULT nextval('posts_sno_seq'::regclass),
    title text COLLATE pg_catalog."default" NOT NULL,
    tagline text COLLATE pg_catalog."default" NOT NULL,
    slug character varying(50) COLLATE pg_catalog."default" NOT NULL,
    href_link character varying(150) COLLATE pg_catalog."default" NOT NULL,
    post_link character varying(150) COLLATE pg_catalog."default" NOT NULL,
    content text COLLATE pg_catalog."default" NOT NULL,
    para text COLLATE pg_catalog."default" NOT NULL,
	cont_one text COLLATE pg_catalog."default" NOT NULL,
	para_one text COLLATE pg_catalog."default" NOT NULL,
	cont_two text COLLATE pg_catalog."default" NOT NULL,
	para_two text COLLATE pg_catalog."default" NOT NULL,
	cont_three text COLLATE pg_catalog."default" NOT NULL,
	para_three text COLLATE pg_catalog."default" NOT NULL,
	cont_four text COLLATE pg_catalog."default" NOT NULL,
	para_four text COLLATE pg_catalog."default" NOT NULL,
    conclusion text COLLATE pg_catalog."default" NOT NULL,
    img_file character varying(50) COLLATE pg_catalog."default" NOT NULL,
    credit text COLLATE pg_catalog."default" NOT NULL,
    post_img character varying(50) COLLATE pg_catalog."default" NOT NULL,
    date date DEFAULT CURRENT_DATE,
    CONSTRAINT posts_pkey PRIMARY KEY (sno)
)
