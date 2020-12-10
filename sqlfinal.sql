PGDMP                 
        x            projeto    13.0    13.0 *    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    32779    projeto    DATABASE     k   CREATE DATABASE projeto WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
    DROP DATABASE projeto;
                postgres    false            �            1259    41046    actors    TABLE     b   CREATE TABLE public.actors (
    actorid integer NOT NULL,
    name text,
    movieid bigint[]
);
    DROP TABLE public.actors;
       public         heap    postgres    false            �            1259    41049    actors_actorid_seq    SEQUENCE     �   CREATE SEQUENCE public.actors_actorid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.actors_actorid_seq;
       public          postgres    false    205            �           0    0    actors_actorid_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.actors_actorid_seq OWNED BY public.actors.actorid;
          public          postgres    false    206            �            1259    49193    messages    TABLE     �   CREATE TABLE public.messages (
    msgid integer NOT NULL,
    message character varying(512),
    bolread boolean,
    users_userid bigint NOT NULL,
    senderid bigint,
    data date
);
    DROP TABLE public.messages;
       public         heap    postgres    false            �            1259    49191    messages_msgid_seq    SEQUENCE     �   CREATE SEQUENCE public.messages_msgid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.messages_msgid_seq;
       public          postgres    false    208            �           0    0    messages_msgid_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.messages_msgid_seq OWNED BY public.messages.msgid;
          public          postgres    false    207            �            1259    32786    movies    TABLE     (  CREATE TABLE public.movies (
    itemid integer NOT NULL,
    name character varying,
    actorid integer NOT NULL,
    director character varying,
    imdbrating double precision,
    genre character varying,
    price double precision,
    year bigint,
    timeavaible bigint,
    type text
);
    DROP TABLE public.movies;
       public         heap    postgres    false            �            1259    32798    movies_actorid_seq    SEQUENCE     �   CREATE SEQUENCE public.movies_actorid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.movies_actorid_seq;
       public          postgres    false    200            �           0    0    movies_actorid_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.movies_actorid_seq OWNED BY public.movies.actorid;
          public          postgres    false    202            �            1259    32789    movies_itemid_seq    SEQUENCE     �   CREATE SEQUENCE public.movies_itemid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.movies_itemid_seq;
       public          postgres    false    200            �           0    0    movies_itemid_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.movies_itemid_seq OWNED BY public.movies.itemid;
          public          postgres    false    201            �            1259    49214    pricehistory    TABLE     j   CREATE TABLE public.pricehistory (
    oldprice real,
    data date,
    movies_itemid bigint NOT NULL
);
     DROP TABLE public.pricehistory;
       public         heap    postgres    false            �            1259    32807    rent    TABLE     �   CREATE TABLE public.rent (
    clientid bigint,
    date timestamp without time zone,
    price real,
    dateend timestamp without time zone,
    usermail text,
    timeavaible bigint,
    orderid integer NOT NULL,
    type text,
    movieid bigint
);
    DROP TABLE public.rent;
       public         heap    postgres    false            �            1259    41008    rent_orderid_seq    SEQUENCE     �   CREATE SEQUENCE public.rent_orderid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.rent_orderid_seq;
       public          postgres    false    203            �           0    0    rent_orderid_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.rent_orderid_seq OWNED BY public.rent.orderid;
          public          postgres    false    204            �            1259    49202    users    TABLE     �   CREATE TABLE public.users (
    userid integer NOT NULL,
    nome text,
    email text,
    password text,
    balance bigint
);
    DROP TABLE public.users;
       public         heap    postgres    false            �            1259    49205    users_userid_seq    SEQUENCE     �   CREATE SEQUENCE public.users_userid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.users_userid_seq;
       public          postgres    false    209            �           0    0    users_userid_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.users_userid_seq OWNED BY public.users.userid;
          public          postgres    false    210            H           2604    41051    actors actorid    DEFAULT     p   ALTER TABLE ONLY public.actors ALTER COLUMN actorid SET DEFAULT nextval('public.actors_actorid_seq'::regclass);
 =   ALTER TABLE public.actors ALTER COLUMN actorid DROP DEFAULT;
       public          postgres    false    206    205            I           2604    49196    messages msgid    DEFAULT     p   ALTER TABLE ONLY public.messages ALTER COLUMN msgid SET DEFAULT nextval('public.messages_msgid_seq'::regclass);
 =   ALTER TABLE public.messages ALTER COLUMN msgid DROP DEFAULT;
       public          postgres    false    207    208    208            E           2604    32791    movies itemid    DEFAULT     n   ALTER TABLE ONLY public.movies ALTER COLUMN itemid SET DEFAULT nextval('public.movies_itemid_seq'::regclass);
 <   ALTER TABLE public.movies ALTER COLUMN itemid DROP DEFAULT;
       public          postgres    false    201    200            F           2604    32800    movies actorid    DEFAULT     p   ALTER TABLE ONLY public.movies ALTER COLUMN actorid SET DEFAULT nextval('public.movies_actorid_seq'::regclass);
 =   ALTER TABLE public.movies ALTER COLUMN actorid DROP DEFAULT;
       public          postgres    false    202    200            G           2604    41010    rent orderid    DEFAULT     l   ALTER TABLE ONLY public.rent ALTER COLUMN orderid SET DEFAULT nextval('public.rent_orderid_seq'::regclass);
 ;   ALTER TABLE public.rent ALTER COLUMN orderid DROP DEFAULT;
       public          postgres    false    204    203            J           2604    49207    users userid    DEFAULT     l   ALTER TABLE ONLY public.users ALTER COLUMN userid SET DEFAULT nextval('public.users_userid_seq'::regclass);
 ;   ALTER TABLE public.users ALTER COLUMN userid DROP DEFAULT;
       public          postgres    false    210    209            �          0    41046    actors 
   TABLE DATA           8   COPY public.actors (actorid, name, movieid) FROM stdin;
    public          postgres    false    205   1,       �          0    49193    messages 
   TABLE DATA           Y   COPY public.messages (msgid, message, bolread, users_userid, senderid, data) FROM stdin;
    public          postgres    false    208   �,       �          0    32786    movies 
   TABLE DATA           t   COPY public.movies (itemid, name, actorid, director, imdbrating, genre, price, year, timeavaible, type) FROM stdin;
    public          postgres    false    200   �,       �          0    49214    pricehistory 
   TABLE DATA           E   COPY public.pricehistory (oldprice, data, movies_itemid) FROM stdin;
    public          postgres    false    211   �-       �          0    32807    rent 
   TABLE DATA           m   COPY public.rent (clientid, date, price, dateend, usermail, timeavaible, orderid, type, movieid) FROM stdin;
    public          postgres    false    203   �-       �          0    49202    users 
   TABLE DATA           G   COPY public.users (userid, nome, email, password, balance) FROM stdin;
    public          postgres    false    209   /       �           0    0    actors_actorid_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.actors_actorid_seq', 1, true);
          public          postgres    false    206            �           0    0    messages_msgid_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.messages_msgid_seq', 2, true);
          public          postgres    false    207            �           0    0    movies_actorid_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.movies_actorid_seq', 1, false);
          public          postgres    false    202            �           0    0    movies_itemid_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.movies_itemid_seq', 2, true);
          public          postgres    false    201            �           0    0    rent_orderid_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.rent_orderid_seq', 45, true);
          public          postgres    false    204            �           0    0    users_userid_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.users_userid_seq', 2, true);
          public          postgres    false    210            N           2606    49201    messages messages_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_pkey PRIMARY KEY (msgid);
 @   ALTER TABLE ONLY public.messages DROP CONSTRAINT messages_pkey;
       public            postgres    false    208            L           2606    41012    rent rent_orderid_key 
   CONSTRAINT     S   ALTER TABLE ONLY public.rent
    ADD CONSTRAINT rent_orderid_key UNIQUE (orderid);
 ?   ALTER TABLE ONLY public.rent DROP CONSTRAINT rent_orderid_key;
       public            postgres    false    203            �   h   x��=
�0���S�D���/X�*�6��pЁ !w�������x���3"�UW�En5�	��ϲkxKS��,f1�t%9�r�x�I/��Z��A�      �   F   x�]ȱ�@��3�:w�!9b�����|������.?c��s��Bà01jCv2��V�c#�M��      �   �   x�m�;�0��zr
� �M^�AIE%�&1b��Fq|�@T��v8ߜ��t�xs�:!?���~3��{��A��B���`	��ę���[�%�$��:�AV�:�?k���RC(R|04�i`�Ђ</9��M1S�/�Ї0���3�c�7V}��"��%ϲ��C>      �      x�34г��4202�54�5 2�b���� 5!�      �     x�m�=N�0Dk��@�����{

$��8�����~���d911m���
�"���� ����F�����O�$�>����/|�qe��^&�g~����L�0�Z�]�����2�Cf+<��EL���|#��!B.�Z(��LE��d�K�,�f��\�%7j-=�ʝ���g�z��Q�d.0��.|�f���B��+)�ݝ���pm����cR�ڮ����My6���!%��2�]���YNf�|K?(�u�7df|���ٓtg��2s����&�lg�^�,�m俅      �   @   x�3�tN,��/VpL*J�+I-�L��RK�r�+���s9�9���8sR+�#K�=... !��     