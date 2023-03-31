--
-- PostgreSQL database dump
--

-- Dumped from database version 14.7 (Ubuntu 14.7-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.7 (Ubuntu 14.7-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: blog; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.blog (
    id integer NOT NULL,
    name character varying(50),
    email character varying(70),
    age integer
);


ALTER TABLE public.blog OWNER TO "user";

--
-- Name: blog_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.blog_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.blog_id_seq OWNER TO "user";

--
-- Name: blog_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.blog_id_seq OWNED BY public.blog.id;


--
-- Name: blogger; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.blogger (
    id integer NOT NULL,
    name character varying(50),
    email character varying(70),
    age integer
);


ALTER TABLE public.blogger OWNER TO "user";

--
-- Name: blogger_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.blogger_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.blogger_id_seq OWNER TO "user";

--
-- Name: blogger_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.blogger_id_seq OWNED BY public.blogger.id;


--
-- Name: post; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.post (
    id integer NOT NULL,
    title character varying(100),
    body text,
    blogger_id integer
);


ALTER TABLE public.post OWNER TO "user";

--
-- Name: post_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.post_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.post_id_seq OWNER TO "user";

--
-- Name: post_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.post_id_seq OWNED BY public.post.id;


--
-- Name: blog id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.blog ALTER COLUMN id SET DEFAULT nextval('public.blog_id_seq'::regclass);


--
-- Name: blogger id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.blogger ALTER COLUMN id SET DEFAULT nextval('public.blogger_id_seq'::regclass);


--
-- Name: post id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.post ALTER COLUMN id SET DEFAULT nextval('public.post_id_seq'::regclass);


--
-- Data for Name: blog; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.blog (id, name, email, age) FROM stdin;
\.


--
-- Data for Name: blogger; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.blogger (id, name, email, age) FROM stdin;
1	bloger1	aa@mail.ru	34
2	bloger2	bb@mail.ru	56
3	bloger3	ccc@mail.ru	76
\.


--
-- Data for Name: post; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.post (id, title, body, blogger_id) FROM stdin;
6	post 1	...	3
7	post 2	aaa	2
8	post 3	---	1
9	post 4	aaaa	1
\.


--
-- Name: blog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.blog_id_seq', 1, false);


--
-- Name: blogger_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.blogger_id_seq', 3, true);


--
-- Name: post_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.post_id_seq', 9, true);


--
-- Name: blogger blogger_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.blogger
    ADD CONSTRAINT blogger_pkey PRIMARY KEY (id);


--
-- Name: post fk_post_blogger; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.post
    ADD CONSTRAINT fk_post_blogger FOREIGN KEY (blogger_id) REFERENCES public.blogger(id);


--
-- PostgreSQL database dump complete
--

