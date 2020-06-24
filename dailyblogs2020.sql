PGDMP     /    (                x            dailyblogs2020    12.3    12.3                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16396    dailyblogs2020    DATABASE     �   CREATE DATABASE dailyblogs2020 WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_India.1252' LC_CTYPE = 'English_India.1252';
    DROP DATABASE dailyblogs2020;
                postgres    false            �            1259    16505    contacts    TABLE     �   CREATE TABLE public.contacts (
    sno integer NOT NULL,
    name text NOT NULL,
    phone_num character varying(50) NOT NULL,
    msg text NOT NULL,
    date date DEFAULT CURRENT_DATE,
    email character varying(50)
);
    DROP TABLE public.contacts;
       public         heap    postgres    false            �            1259    16503    contacts_sno_seq    SEQUENCE     �   CREATE SEQUENCE public.contacts_sno_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.contacts_sno_seq;
       public          postgres    false    204                       0    0    contacts_sno_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.contacts_sno_seq OWNED BY public.contacts.sno;
          public          postgres    false    203            �            1259    16431    posts    TABLE     �   CREATE TABLE public.posts (
    sno integer,
    title text,
    tagline text,
    slug character varying(25),
    content text,
    img_file character varying(25),
    credit text,
    date date,
    post_img character varying(50)
);
    DROP TABLE public.posts;
       public         heap    postgres    false            �
           2604    16508    contacts sno    DEFAULT     l   ALTER TABLE ONLY public.contacts ALTER COLUMN sno SET DEFAULT nextval('public.contacts_sno_seq'::regclass);
 ;   ALTER TABLE public.contacts ALTER COLUMN sno DROP DEFAULT;
       public          postgres    false    204    203    204            	          0    16505    contacts 
   TABLE DATA           J   COPY public.contacts (sno, name, phone_num, msg, date, email) FROM stdin;
    public          postgres    false    204   �                 0    16431    posts 
   TABLE DATA           e   COPY public.posts (sno, title, tagline, slug, content, img_file, credit, date, post_img) FROM stdin;
    public          postgres    false    202   *                  0    0    contacts_sno_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.contacts_sno_seq', 9, true);
          public          postgres    false    203            �
           2606    16514    contacts contacts_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY public.contacts
    ADD CONSTRAINT contacts_pkey PRIMARY KEY (sno);
 @   ALTER TABLE ONLY public.contacts DROP CONSTRAINT contacts_pkey;
       public            postgres    false    204            	   �   x�3�,I-.�4��AΌ��T����b��̜����lN##]3]#�r��������\.#
�S�"�`�if��&$��c5��S*�cF%s̩d$<9Ma[�*��)��!��#dI-�b���� ���8         �  x��X]���|^���H���N�X���` N|H`��^�d�r��33�5��S�=�r��8:�ș����n��ͽͽ�.V���~ؼy?�H>����zW���h��<7U�ꐳy�:O��C3�9mʋ]�/���Y㒱���q2���-?:�p���q�E2]8�p�1��bto�]��]n��q�̙"�19�)��C��n�N"�X���N���-[8�Л��d�M�%�8��j6{�1~�Z��1�sn�t�P|�'SM��B����'�bC�����D�)��.�����|��K�o���*Ć�i\�L[>q��|`���sp���9p"V8N8���Ύ��������������cSQ>y�)����&�Ëc`��V"�Fd.s����)2��u76ĳ�ޢ ��=���zoJ0�����x�$����������4_�����˃���Rp�p�`��OJ�9���1Q�pmO�   �18����\H�	�ɔ� �p'��ݲA_j+vl�mR�jm�[j8l�1UHj��H�ͺ�_#���	˸���C�!ד ��H�Ndއ|I�f�FT��at4r�1��vpp$Ƥ�0�	نm�R���E !^�� 3�y%$L����6���&�"[ }l,j��"�C���1�{�.3�ί�j�_P�?�Nq�ҷh�5����
�[�B��RZ�˿��C�VԆ�yI���{�"�� �5�p)N5N��� ����dH��lF���O��vnk~��T��P��ۯ��%	sn���u[�A��V1�Q�N�i4.�bjTzJh�V��@ƃ�(x�7^.�d�a���۹���B��B�Ҹ���c��_�rB�*ʅ�Ֆ����p ��
��|eJ��\I��o�t��~�X19�oף_'�4�<�k��O�qs���o�^ݽڽ�~w�fӆ�vՑ_>����	&��Rq�76fm:�]7�m��wx�)_��rL*$��6a�J�
��a����|v'6�V�|�{��"�q��@�BY��WW`�7�V�W6ß�U�� ��M3
�F\�d� ,{$�L:!B,�)H4�)[ub���4Cax���"�	�����u�Tێ��]�
��K�r��z1�Zs�W�����0��������7�?�DkIu��ۀ�����>��/�V:�Y6���ŏ��Y'^�
Q5�2����Z=r�;�]�ʠ �t?��(�L�2oL\ƞ��ޝ���MI>�Q�'�s�6ϊ�>�:_
��dR�b� ����5b��b�^P�Aa �uV܊	i��$����9	M���a3�HO�T�t��l���]3a�*kyh�뗼S�t[��E�W_�]�Cs@�y�֣k�#��5T���H�Ѻ��iǞa�+�҇G|F<�J%�	w� 5?S��_d��T����aD0�,��� ��z�&Q���e��\w!�0)\�J�r�%����;@w�sG?��$r&�('�ܽ�����P]�sZ6���.f�F�J��d&NkG�&�>�j̇�l��ƃ�l�:��`_L)�xqB1�F�Hc���r��pS����zR=�l*�a䅍� �,y��2�q2�݊ �E���+,�:��UQ�",)����'���lcD��Kt��.��%����Y�� :_-�k�E/�^�G�����v��C�AE��gЇ�r�5�HY?��f��f�m����5���Y^W�Fx�Ve���#R(lG s^����z��_ �?y[�x��*z:_�zE��Le�����Z{݃�o�@R"c�e��V>�d��j�7��8?��cS5d���_s����;&3�"{:a�1(?���D��J��m�����/���W!�����ʻ�LFb㼑�^�խ@Kjkh.�7cE�����9��h=����Y<[H�;_$���e��Yd��|nm�$��u%T��h����͘ͼ��m���j	|���84̆���a_�?�&�l�Z�!Ǎ (<�~���{f�|����_�ϟ/��Ϟ=�/���a     