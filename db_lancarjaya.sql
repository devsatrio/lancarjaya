-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 02 Feb 2020 pada 15.56
-- Versi server: 10.4.11-MariaDB
-- Versi PHP: 7.3.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_lancarjaya`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL PRIMARY KEY,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add barang', 7, 'add_barang'),
(26, 'Can change barang', 7, 'change_barang'),
(27, 'Can delete barang', 7, 'delete_barang'),
(28, 'Can view barang', 7, 'view_barang'),
(29, 'Can add kategori', 8, 'add_kategori'),
(30, 'Can change kategori', 8, 'change_kategori'),
(31, 'Can delete kategori', 8, 'delete_kategori'),
(32, 'Can view kategori', 8, 'view_kategori'),
(33, 'Can add kategori', 9, 'add_kategori'),
(34, 'Can change kategori', 9, 'change_kategori'),
(35, 'Can delete kategori', 9, 'delete_kategori'),
(36, 'Can view kategori', 9, 'view_kategori'),
(37, 'Can add artikel', 10, 'add_artikel'),
(38, 'Can change artikel', 10, 'change_artikel'),
(39, 'Can delete artikel', 10, 'delete_artikel'),
(40, 'Can view artikel', 10, 'view_artikel'),
(41, 'Can add kategori', 11, 'add_kategori'),
(42, 'Can change kategori', 11, 'change_kategori'),
(43, 'Can delete kategori', 11, 'delete_kategori'),
(44, 'Can view kategori', 11, 'view_kategori'),
(45, 'Can add foto', 12, 'add_foto'),
(46, 'Can change foto', 12, 'change_foto'),
(47, 'Can delete foto', 12, 'delete_foto'),
(48, 'Can view foto', 12, 'view_foto'),
(49, 'Can add contact', 13, 'add_contact'),
(50, 'Can change contact', 13, 'change_contact'),
(51, 'Can delete contact', 13, 'delete_contact'),
(52, 'Can view contact', 13, 'view_contact'),
(53, 'Can add gambar', 14, 'add_gambar'),
(54, 'Can change gambar', 14, 'change_gambar'),
(55, 'Can delete gambar', 14, 'delete_gambar'),
(56, 'Can view gambar', 14, 'view_gambar'),
(57, 'Can add testi', 15, 'add_testi'),
(58, 'Can change testi', 15, 'change_testi'),
(59, 'Can delete testi', 15, 'delete_testi'),
(60, 'Can view testi', 15, 'view_testi');

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$150000$eefAxJeok7LT$fnOH+xGq2Cc1HazBPhSe8bY5n1mR3HntVTjm0Jfp0O8=', '2020-02-02 12:48:25.219847', 1, 'devasatrio', 'deva', 'satrio', 'satriosuklun@gmail.com', 1, 1, '2020-01-23 01:56:28.000000');

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `blog_artikel`
--

CREATE TABLE `blog_artikel` (
  `id` int(11) NOT NULL,
  `judul` varchar(50) NOT NULL,
  `isi` longtext NOT NULL,
  `tanggal` datetime(6) DEFAULT NULL,
  `slug` varchar(50) DEFAULT NULL,
  `gambar` varchar(100) DEFAULT NULL,
  `kategori_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `blog_artikel`
--

INSERT INTO `blog_artikel` (`id`, `judul`, `isi`, `tanggal`, `slug`, `gambar`, `kategori_id`) VALUES
(1, 'artikel satu', 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Enim optio quisquam id aspernatur, ipsam eaque nemo quas quasi inventore soluta, dolorem earum aperiam porro facere cupiditate quod nesciunt voluptatem explicabo? Lorem, ipsum dolor sit amet consectetur adipisicing elit. Enim optio quisquam id aspernatur, ipsam eaque nemo quas quasi inventore soluta, dolorem earum aperiam porro facere cupiditate quod nesciunt voluptatem explicabo?\r\nLorem, ipsum dolor sit amet consectetur adipisicing elit. Enim optio quisquam id aspernatur, ipsam eaque nemo quas quasi inventore soluta, dolorem earum aperiam porro facere cupiditate quod nesciunt voluptatem explicabo?\r\n\r\nLorem, ipsum dolor sit amet consectetur adipisicing elit. Enim optio quisquam id aspernatur, ipsam eaque nemo quas quasi inventore soluta, dolorem earum aperiam porro facere cupiditate quod nesciunt voluptatem explicabo?', '2020-02-01 13:36:26.714977', 'artikel-satu', 'artikel/blog1.png', 1),
(2, 'artikel dua', 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Rerum quae nobis impedit, veniam at ipsam, fugiat cum modi quis unde fugit, quas animi non suscipit esse aut accusamus error? Dolore!Lorem ipsum dolor sit amet consectetur, adipisicing elit. Rerum quae nobis impedit, veniam at ipsam, fugiat cum modi quis unde fugit, quas animi non suscipit esse aut accusamus error? Dolore!Lorem ipsum dolor sit amet consectetur, adipisicing elit. Rerum quae nobis impedit, veniam at ipsam, fugiat cum modi quis unde fugit, quas animi non suscipit esse aut accusamus error? Dolore!\r\n\r\nLorem ipsum dolor sit amet consectetur, adipisicing elit. Rerum quae nobis impedit, veniam at ipsam, fugiat cum modi quis unde fugit, quas animi non suscipit esse aut accusamus error? Dolore!\r\nLorem ipsum dolor sit amet consectetur, adipisicing elit. Rerum quae nobis impedit, veniam at ipsam, fugiat cum modi quis unde fugit, quas animi non suscipit esse aut accusamus error? Dolore!Lorem ipsum dolor sit', '2020-02-01 13:41:18.299648', 'artikel-dua', 'artikel/blog2.png', 2),
(3, 'artikel tiga', 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Rerum quae nobis impedit, veniam at ipsam, fugiat cum modi quis unde fugit, quas animi non suscipit esse aut accusamus error? Dolore!Lorem ipsum dolor sit amet consectetur, adipisicing elit. Rerum quae nobis impedit, veniam at ipsam, fugiat cum modi quis unde fugit, quas animi non suscipit esse aut accusamus error? Dolore!\r\n\r\nLorem ipsum dolor sit amet consectetur, adipisicing elit. Rerum quae nobis impedit, veniam at ipsam, fugiat cum modi quis unde fugit, quas animi non suscipit esse aut accusamus error? Dolore!Lorem ipsum dolor sit amet consectetur, adipisicing elit. Rerum quae nobis impedit, veniam at ipsam, fugiat cum modi quis unde fugit, quas animi non suscipit esse aut accusamus error? Dolore!', '2020-02-01 13:41:37.200200', 'artikel-tiga', 'artikel/blog3.png', 3);

-- --------------------------------------------------------

--
-- Struktur dari tabel `blog_kategori`
--

CREATE TABLE `blog_kategori` (
  `id` int(11) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `tanggal` datetime(6) NOT NULL,
  `slug` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `blog_kategori`
--

INSERT INTO `blog_kategori` (`id`, `nama`, `tanggal`, `slug`) VALUES
(1, 'Informasi', '2020-02-01 13:34:33.525239', 'informasi'),
(2, 'Berita', '2020-02-01 13:35:04.635617', 'berita'),
(3, 'Cerita', '2020-02-01 13:35:10.202419', 'cerita');

-- --------------------------------------------------------

--
-- Struktur dari tabel `contact_contact`
--

CREATE TABLE `contact_contact` (
  `id` int(11) NOT NULL,
  `nomer_hp_dua` varchar(20) NOT NULL,
  `nomer_hp_satu` varchar(20) NOT NULL,
  `alamat` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `deskripsi` longtext NOT NULL,
  `facebook` varchar(100) NOT NULL,
  `instagram` varchar(100) NOT NULL,
  `moto` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `contact_contact`
--

INSERT INTO `contact_contact` (`id`, `nomer_hp_dua`, `nomer_hp_satu`, `alamat`, `email`, `deskripsi`, `facebook`, `instagram`, `moto`) VALUES
(2, '08198475899', '08560703948', 'Proin fringilla augue at maximus vestibulum', 'satriosuklun@gmail.com', 'Proin fringilla augue at maximus vestibulum. Nam pulvinar vitae neque et porttitor. Praesent sed nisi eleifend, lorem fermentum orci sit amet, iaculis libero', 'lambe_turah', '@lambe_Turah', 'Proin fringilla augue at maximus vestibulum.');

-- --------------------------------------------------------

--
-- Struktur dari tabel `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2020-01-23 01:57:16.246333', '1', 'devasatrio', 2, '[{\"changed\": {\"fields\": [\"first_name\", \"last_name\"]}}]', 4, 1),
(2, '2020-01-23 03:45:22.751359', '1', 'baju koko', 1, '[{\"added\": {}}]', 8, 1),
(3, '2020-01-23 03:45:28.523829', '1', 'asdfsda', 1, '[{\"added\": {}}]', 7, 1),
(4, '2020-01-23 04:38:06.533330', '1', 'asdfsda', 3, '', 7, 1),
(5, '2020-01-23 04:38:15.920107', '1', 'baju koko', 3, '', 8, 1),
(6, '2020-01-23 04:39:16.315332', '2', 'Berita', 1, '[{\"added\": {}}]', 8, 1),
(7, '2020-01-23 04:39:44.183559', '2', 'Baju Cewek', 2, '[{\"changed\": {\"fields\": [\"nama\"]}}]', 8, 1),
(8, '2020-01-23 04:40:31.459238', '3', 'Baju Cowok', 1, '[{\"added\": {}}]', 8, 1),
(9, '2020-01-23 04:42:51.244803', '2', 'hoodie cowok mantab jiwa', 1, '[{\"added\": {}}]', 7, 1),
(10, '2020-01-27 03:17:13.682883', '2', 'hoodie cowok mantab jiwa', 2, '[{\"changed\": {\"fields\": [\"gambar\"]}}]', 7, 1),
(11, '2020-01-27 03:18:07.920101', '3', 'barang mantab', 1, '[{\"added\": {}}]', 7, 1),
(12, '2020-01-27 03:18:46.281605', '2', 'hoodie cowok mantab jiwa', 2, '[{\"changed\": {\"fields\": [\"gambar\"]}}]', 7, 1),
(13, '2020-01-27 14:30:11.495614', '1', 'deni', 1, '[{\"added\": {}}]', 15, 1),
(14, '2020-02-01 13:34:35.008505', '1', 'Informasi', 1, '[{\"added\": {}}]', 9, 1),
(15, '2020-02-01 13:35:04.731323', '2', 'Berita', 1, '[{\"added\": {}}]', 9, 1),
(16, '2020-02-01 13:35:10.302706', '3', 'Cerita', 1, '[{\"added\": {}}]', 9, 1),
(17, '2020-02-01 13:36:26.726642', '1', 'artikel satu', 1, '[{\"added\": {}}]', 10, 1),
(18, '2020-02-01 13:41:18.394748', '2', 'artikel dua', 1, '[{\"added\": {}}]', 10, 1),
(19, '2020-02-01 13:41:37.840019', '3', 'artikel tiga', 1, '[{\"added\": {}}]', 10, 1),
(20, '2020-02-02 12:51:00.463978', '1', 'Kegiatan', 1, '[{\"added\": {}}]', 11, 1),
(21, '2020-02-02 12:51:26.410637', '2', 'Testimoni', 1, '[{\"added\": {}}]', 11, 1),
(22, '2020-02-02 12:51:36.328040', '3', 'Liburan', 1, '[{\"added\": {}}]', 11, 1),
(23, '2020-02-02 12:55:08.941297', '1', 'Foto satu', 1, '[{\"added\": {}}]', 12, 1),
(24, '2020-02-02 12:55:29.349738', '2', 'foto dua', 1, '[{\"added\": {}}]', 12, 1),
(25, '2020-02-02 12:55:43.708834', '3', 'foto tiga', 1, '[{\"added\": {}}]', 12, 1),
(26, '2020-02-02 12:55:56.290725', '4', 'foto empat', 1, '[{\"added\": {}}]', 12, 1),
(27, '2020-02-02 12:57:11.311514', '3', 'barang satu', 2, '[{\"changed\": {\"fields\": [\"nama\", \"deskripsi\"]}}]', 7, 1),
(28, '2020-02-02 12:57:27.411309', '2', 'barang dua', 2, '[{\"changed\": {\"fields\": [\"nama\", \"deskripsi\"]}}]', 7, 1),
(29, '2020-02-02 12:58:45.226372', '4', 'barang tiga', 1, '[{\"added\": {}}]', 7, 1),
(30, '2020-02-02 12:59:39.536070', '5', 'barang empat', 1, '[{\"added\": {}}]', 7, 1),
(31, '2020-02-02 13:00:06.434683', '6', 'barang lima', 1, '[{\"added\": {}}]', 7, 1),
(32, '2020-02-02 13:00:54.534065', '7', 'barang enam', 1, '[{\"added\": {}}]', 7, 1),
(33, '2020-02-02 13:01:22.214077', '8', 'barang tujuh', 1, '[{\"added\": {}}]', 7, 1),
(34, '2020-02-02 13:02:21.018155', '1', 'Slide Satu', 1, '[{\"added\": {}}]', 14, 1),
(35, '2020-02-02 13:02:36.427527', '2', 'Slider dua', 1, '[{\"added\": {}}]', 14, 1),
(36, '2020-02-02 13:16:24.670023', '2', 'Lorem ipsum dolor', 2, '[{\"changed\": {\"fields\": [\"head\", \"deskripsi\"]}}]', 14, 1),
(37, '2020-02-02 13:16:50.107152', '1', 'consectetur adipisicing elit', 2, '[{\"changed\": {\"fields\": [\"head\", \"deskripsi\"]}}]', 14, 1),
(38, '2020-02-02 13:38:52.690684', '1', 'Deva', 1, '[{\"added\": {}}]', 13, 1),
(39, '2020-02-02 13:39:54.839086', '1', 'Deva', 2, '[]', 13, 1),
(40, '2020-02-02 13:56:22.929047', '2', 'Proin fringilla augue at maximus vestibulum.', 1, '[{\"added\": {}}]', 13, 1),
(41, '2020-02-02 14:30:16.376349', '2', 'Proin fringilla augue at maximus vestibulum.', 2, '[{\"changed\": {\"fields\": [\"alamat\"]}}]', 13, 1);

-- --------------------------------------------------------

--
-- Struktur dari tabel `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(10, 'blog', 'artikel'),
(9, 'blog', 'kategori'),
(13, 'contact', 'contact'),
(5, 'contenttypes', 'contenttype'),
(12, 'galeri', 'foto'),
(11, 'galeri', 'kategori'),
(7, 'produk', 'barang'),
(8, 'produk', 'kategori'),
(6, 'sessions', 'session'),
(14, 'slider', 'gambar'),
(15, 'testimoni', 'testi');

-- --------------------------------------------------------

--
-- Struktur dari tabel `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-01-23 01:55:36.151975'),
(2, 'auth', '0001_initial', '2020-01-23 01:55:37.696331'),
(3, 'admin', '0001_initial', '2020-01-23 01:55:45.540515'),
(4, 'admin', '0002_logentry_remove_auto_add', '2020-01-23 01:55:47.249136'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2020-01-23 01:55:47.289140'),
(6, 'contenttypes', '0002_remove_content_type_name', '2020-01-23 01:55:47.981494'),
(7, 'auth', '0002_alter_permission_name_max_length', '2020-01-23 01:55:48.457494'),
(8, 'auth', '0003_alter_user_email_max_length', '2020-01-23 01:55:48.513494'),
(9, 'auth', '0004_alter_user_username_opts', '2020-01-23 01:55:48.537528'),
(10, 'auth', '0005_alter_user_last_login_null', '2020-01-23 01:55:48.889612'),
(11, 'auth', '0006_require_contenttypes_0002', '2020-01-23 01:55:48.901608'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2020-01-23 01:55:48.921559'),
(13, 'auth', '0008_alter_user_username_max_length', '2020-01-23 01:55:48.981525'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2020-01-23 01:55:49.049588'),
(15, 'auth', '0010_alter_group_name_max_length', '2020-01-23 01:55:49.113559'),
(16, 'auth', '0011_update_proxy_permissions', '2020-01-23 01:55:49.133558'),
(17, 'sessions', '0001_initial', '2020-01-23 01:55:49.585782'),
(18, 'produk', '0001_initial', '2020-01-23 03:04:37.529511'),
(19, 'produk', '0002_auto_20200123_1136', '2020-01-23 04:37:45.570260'),
(20, 'blog', '0001_initial', '2020-01-27 02:29:19.204296'),
(21, 'blog', '0002_auto_20200123_1146', '2020-01-27 02:29:20.256584'),
(22, 'blog', '0003_auto_20200123_1229', '2020-01-27 02:29:20.544719'),
(23, 'blog', '0004_auto_20200123_1317', '2020-01-27 02:29:20.564726'),
(24, 'contact', '0001_initial', '2020-01-27 02:29:20.688690'),
(25, 'galeri', '0001_initial', '2020-01-27 02:29:20.888776'),
(26, 'galeri', '0002_auto_20200123_1209', '2020-01-27 02:29:21.357088'),
(27, 'galeri', '0003_foto_kategori', '2020-01-27 02:29:22.593465'),
(28, 'produk', '0003_auto_20200123_1427', '2020-01-27 02:29:23.341492'),
(29, 'produk', '0003_auto_20200123_1326', '2020-01-27 02:29:23.377465'),
(30, 'produk', '0004_merge_20200123_1538', '2020-01-27 02:29:23.405509'),
(31, 'slider', '0001_initial', '2020-01-27 02:29:23.557465'),
(32, 'produk', '0005_barang_gambar', '2020-01-27 03:11:52.043853'),
(33, 'testimoni', '0001_initial', '2020-01-27 14:26:57.637548'),
(34, 'contact', '0002_remove_contact_slug', '2020-02-02 13:15:08.551264'),
(35, 'slider', '0002_auto_20200202_2012', '2020-02-02 13:15:08.737606'),
(36, 'contact', '0003_auto_20200202_2043', '2020-02-02 13:52:45.239026'),
(37, 'contact', '0004_auto_20200202_2056', '2020-02-02 13:56:15.075838');

-- --------------------------------------------------------

--
-- Struktur dari tabel `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('6gvsbgq2moqnj6vddje64zbr7pzm69c0', 'ZTc4NDAyYzY2NTYxZjBjYWRjMWE3OGM4YTZmMGQ4Njg5YzAzNTdmYTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiOGRkY2Y3MDY1Yjg0OWY0NTYyMWRjZTRkMGY1OTZlNjc3YzU0OWY3In0=', '2020-02-15 13:32:55.966617'),
('elhk37s70g14xgjirzwxsay3w1pysef1', 'ZTc4NDAyYzY2NTYxZjBjYWRjMWE3OGM4YTZmMGQ4Njg5YzAzNTdmYTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiOGRkY2Y3MDY1Yjg0OWY0NTYyMWRjZTRkMGY1OTZlNjc3YzU0OWY3In0=', '2020-02-06 03:53:48.356812'),
('j2sx8cwaakbm3egshrlzd9r3bw8mua3o', 'ZTc4NDAyYzY2NTYxZjBjYWRjMWE3OGM4YTZmMGQ4Njg5YzAzNTdmYTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiOGRkY2Y3MDY1Yjg0OWY0NTYyMWRjZTRkMGY1OTZlNjc3YzU0OWY3In0=', '2020-02-10 02:34:39.492754'),
('w7lu2mqtawi5hrinwx6i4rx406tfbpjd', 'ZTc4NDAyYzY2NTYxZjBjYWRjMWE3OGM4YTZmMGQ4Njg5YzAzNTdmYTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiOGRkY2Y3MDY1Yjg0OWY0NTYyMWRjZTRkMGY1OTZlNjc3YzU0OWY3In0=', '2020-02-06 01:56:58.378782'),
('y8fc2wxhhok36z19g6yyjick97z6p65b', 'ZTc4NDAyYzY2NTYxZjBjYWRjMWE3OGM4YTZmMGQ4Njg5YzAzNTdmYTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiOGRkY2Y3MDY1Yjg0OWY0NTYyMWRjZTRkMGY1OTZlNjc3YzU0OWY3In0=', '2020-02-10 14:27:36.496446'),
('yn1jvbe6ypxfm6mrupndzkqubtdclnke', 'ZTc4NDAyYzY2NTYxZjBjYWRjMWE3OGM4YTZmMGQ4Njg5YzAzNTdmYTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiOGRkY2Y3MDY1Yjg0OWY0NTYyMWRjZTRkMGY1OTZlNjc3YzU0OWY3In0=', '2020-02-16 12:48:25.282829');

-- --------------------------------------------------------

--
-- Struktur dari tabel `galeri_foto`
--

CREATE TABLE `galeri_foto` (
  `id` int(11) NOT NULL,
  `judul` varchar(50) NOT NULL,
  `deskripsi` longtext NOT NULL,
  `gambar` varchar(100) DEFAULT NULL,
  `tanggal` datetime(6) DEFAULT NULL,
  `slug` varchar(50) DEFAULT NULL,
  `kategori_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `galeri_foto`
--

INSERT INTO `galeri_foto` (`id`, `judul`, `deskripsi`, `gambar`, `tanggal`, `slug`, `kategori_id`) VALUES
(1, 'Foto satu', 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolor non ipsa beatae', 'foto/1.jpg', '2020-02-02 12:55:08.929517', 'foto-satu', 1),
(2, 'foto dua', 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolor non ipsa beatae', 'foto/2.jpg', '2020-02-02 12:55:29.311755', 'foto-dua', 2),
(3, 'foto tiga', 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolor non ipsa beatae', 'foto/3.jpg', '2020-02-02 12:55:43.686670', 'foto-tiga', 2),
(4, 'foto empat', 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolor non ipsa beatae', 'foto/4.jpg', '2020-02-02 12:55:56.157238', 'foto-empat', 3);

-- --------------------------------------------------------

--
-- Struktur dari tabel `galeri_kategori`
--

CREATE TABLE `galeri_kategori` (
  `id` int(11) NOT NULL,
  `tanggal_buat` datetime(6) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `slug` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `galeri_kategori`
--

INSERT INTO `galeri_kategori` (`id`, `tanggal_buat`, `nama`, `slug`) VALUES
(1, '2020-02-02 12:51:00.412136', 'Kegiatan', 'kegiatan'),
(2, '2020-02-02 12:51:25.997406', 'Testimoni', 'testimoni'),
(3, '2020-02-02 12:51:36.290173', 'Liburan', 'liburan');

-- --------------------------------------------------------

--
-- Struktur dari tabel `produk_barang`
--

CREATE TABLE `produk_barang` (
  `id` int(11) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `deskripsi` longtext NOT NULL,
  `harga` int(11) NOT NULL,
  `diskon` int(11) NOT NULL,
  `tanggal_buat` datetime(6) NOT NULL,
  `kategori_id` int(11) DEFAULT NULL,
  `slug` varchar(50) DEFAULT NULL,
  `gambar` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `produk_barang`
--

INSERT INTO `produk_barang` (`id`, `nama`, `deskripsi`, `harga`, `diskon`, `tanggal_buat`, `kategori_id`, `slug`, `gambar`) VALUES
(2, 'barang dua', 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolor non ipsa beatae', 40000, 0, '2020-01-23 04:42:51.048739', 3, 'barang-dua', 'produk/product1.png'),
(3, 'barang satu', 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolor non ipsa beatae', 20000, 10, '2020-01-27 03:18:07.834303', 3, 'barang-satu', 'produk/product5.png'),
(4, 'barang tiga', 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolor non ipsa beatae', 45000, 0, '2020-02-02 12:58:45.224831', 3, 'barang-tiga', 'produk/product4.png'),
(5, 'barang empat', 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolor non ipsa beatae', 50000, 10, '2020-02-02 12:59:39.534101', 3, 'barang-empat', 'produk/product5_42cjm0q.png'),
(6, 'barang lima', 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolor non ipsa beatae', 35000, 10, '2020-02-02 13:00:06.003275', 3, 'barang-lima', 'produk/product3.png'),
(7, 'barang enam', 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolor non ipsa beatae', 57000, 0, '2020-02-02 13:00:54.015302', 3, 'barang-enam', 'produk/product2.png'),
(8, 'barang tujuh', 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolor non ipsa beatae', 65000, 0, '2020-02-02 13:01:22.059285', 3, 'barang-tujuh', 'produk/product7.png');

-- --------------------------------------------------------

--
-- Struktur dari tabel `produk_kategori`
--

CREATE TABLE `produk_kategori` (
  `id` int(11) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `tanggal_buat` datetime(6) NOT NULL,
  `slug` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `produk_kategori`
--

INSERT INTO `produk_kategori` (`id`, `nama`, `tanggal_buat`, `slug`) VALUES
(2, 'Baju Cewek', '2020-01-23 04:39:16.067250', 'baju-cewek'),
(3, 'Baju Cowok', '2020-01-23 04:40:31.395008', 'baju-cowok');

-- --------------------------------------------------------

--
-- Struktur dari tabel `slider_gambar`
--

CREATE TABLE `slider_gambar` (
  `id` int(11) NOT NULL,
  `head` varchar(35) NOT NULL,
  `gambar` varchar(100) DEFAULT NULL,
  `deskripsi` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `slider_gambar`
--

INSERT INTO `slider_gambar` (`id`, `head`, `gambar`, `deskripsi`) VALUES
(1, 'consectetur adipisicing elit', 'slider/bg-2.jpg', 'vitae eligendi reiciendis incidunt repellendus obcaecati molestias? Porro!'),
(2, 'Lorem ipsum dolor', 'slider/bg.jpg', 'Ad doloribus perferendis quibusdam dolorum consequuntur sed qui perspiciatis');

-- --------------------------------------------------------

--
-- Struktur dari tabel `testimoni_testi`
--

CREATE TABLE `testimoni_testi` (
  `id` int(11) NOT NULL,
  `nama` varchar(80) NOT NULL,
  `email` varchar(254) NOT NULL,
  `perihal` varchar(100) NOT NULL,
  `deskripsi` longtext NOT NULL,
  `tanggal_buat` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `testimoni_testi`
--

INSERT INTO `testimoni_testi` (`id`, `nama`, `email`, `perihal`, `deskripsi`, `tanggal_buat`) VALUES
(1, 'deni', 'satriosuklun1@gmail.com', 'pengiriman', 'pengirman sangat cepat dan terpercaya', '2020-01-27 14:30:11.391919'),
(2, 'deva', 'satriosuklun@gmail.com', 'pengiriman', 'halo halo halo', '2020-01-28 01:53:54.936877'),
(3, 'asfdsad', 'saddfsa', 'sadfsd', 'sadfsad', '2020-01-28 01:55:29.106899'),
(4, 'sadf', 'sadf', 'sdf', 'asdfdsaf', '2020-01-28 02:00:06.345282'),
(5, 'asdfads', 'sadfsa', 'sakdf', 'klsadfj', '2020-01-28 02:05:43.995770'),
(6, 'sfsa', 'ksadjf', 'sdaf', 'skaldfj', '2020-01-28 02:07:07.104213'),
(7, 'asdf', 'sdf', 'sadf', 'sdafsadf', '2020-01-28 02:09:09.277086'),
(8, 'asdf', 'sadfas', 'sadf', 'asdfsaf', '2020-01-28 02:10:19.895259'),
(9, 'asdfads', 'sadfsa', 'sadfsaf', 'sadfdsf', '2020-01-28 02:11:38.399961'),
(10, 'sadf', 'sadf', 'sadf', 'asdfdsaf', '2020-01-28 02:12:13.317366'),
(11, 'deva', 'satriosuklun@gmail.com', 'perngiriman', 'coba coba', '2020-01-28 02:29:05.764307');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `auth_group`
--
ALTER TABLE `auth_group`
  ADD UNIQUE KEY `name` (`name`);

--
-- Indeks untuk tabel `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indeks untuk tabel `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indeks untuk tabel `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indeks untuk tabel `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indeks untuk tabel `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indeks untuk tabel `blog_artikel`
--
ALTER TABLE `blog_artikel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `blog_artikel_judul_d57e0de8_uniq` (`judul`),
  ADD KEY `blog_artikel_kategori_id_d850ff1f_fk_blog_kategori_id` (`kategori_id`),
  ADD KEY `blog_artikel_slug_73a9d6d3` (`slug`);

--
-- Indeks untuk tabel `blog_kategori`
--
ALTER TABLE `blog_kategori`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `blog_kategori_nama_20f5dcaa_uniq` (`nama`),
  ADD KEY `blog_kategori_slug_92bd33f7` (`slug`);

--
-- Indeks untuk tabel `contact_contact`
--
ALTER TABLE `contact_contact`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indeks untuk tabel `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indeks untuk tabel `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indeks untuk tabel `galeri_foto`
--
ALTER TABLE `galeri_foto`
  ADD PRIMARY KEY (`id`),
  ADD KEY `galeri_foto_slug_0b24ed05` (`slug`),
  ADD KEY `galeri_foto_kategori_id_f7ff1209_fk_galeri_kategori_id` (`kategori_id`);

--
-- Indeks untuk tabel `galeri_kategori`
--
ALTER TABLE `galeri_kategori`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nama` (`nama`),
  ADD KEY `galeri_kategori_slug_bfca5cbb` (`slug`);

--
-- Indeks untuk tabel `produk_barang`
--
ALTER TABLE `produk_barang`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `produk_barang_nama_1a6f3761_uniq` (`nama`),
  ADD KEY `produk_barang_kategori_id_5d347768_fk_produk_kategori_id` (`kategori_id`),
  ADD KEY `produk_barang_slug_e1fb6260` (`slug`);

--
-- Indeks untuk tabel `produk_kategori`
--
ALTER TABLE `produk_kategori`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `produk_kategori_nama_16d501e0_uniq` (`nama`),
  ADD KEY `produk_kategori_slug_00cd7d33` (`slug`);

--
-- Indeks untuk tabel `slider_gambar`
--
ALTER TABLE `slider_gambar`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `testimoni_testi`
--
ALTER TABLE `testimoni_testi`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT untuk tabel `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT untuk tabel `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `blog_artikel`
--
ALTER TABLE `blog_artikel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT untuk tabel `blog_kategori`
--
ALTER TABLE `blog_kategori`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT untuk tabel `contact_contact`
--
ALTER TABLE `contact_contact`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT untuk tabel `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT untuk tabel `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT untuk tabel `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT untuk tabel `galeri_foto`
--
ALTER TABLE `galeri_foto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `galeri_kategori`
--
ALTER TABLE `galeri_kategori`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT untuk tabel `produk_barang`
--
ALTER TABLE `produk_barang`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT untuk tabel `produk_kategori`
--
ALTER TABLE `produk_kategori`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT untuk tabel `slider_gambar`
--
ALTER TABLE `slider_gambar`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT untuk tabel `testimoni_testi`
--
ALTER TABLE `testimoni_testi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `auth_group_permissions`
--
/*ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);*/

--
-- Ketidakleluasaan untuk tabel `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Ketidakleluasaan untuk tabel `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ketidakleluasaan untuk tabel `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ketidakleluasaan untuk tabel `blog_artikel`
--
ALTER TABLE `blog_artikel`
  ADD CONSTRAINT `blog_artikel_kategori_id_d850ff1f_fk_blog_kategori_id` FOREIGN KEY (`kategori_id`) REFERENCES `blog_kategori` (`id`);

--
-- Ketidakleluasaan untuk tabel `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ketidakleluasaan untuk tabel `galeri_foto`
--
ALTER TABLE `galeri_foto`
  ADD CONSTRAINT `galeri_foto_kategori_id_f7ff1209_fk_galeri_kategori_id` FOREIGN KEY (`kategori_id`) REFERENCES `galeri_kategori` (`id`);

--
-- Ketidakleluasaan untuk tabel `produk_barang`
--
ALTER TABLE `produk_barang`
  ADD CONSTRAINT `produk_barang_kategori_id_5d347768_fk_produk_kategori_id` FOREIGN KEY (`kategori_id`) REFERENCES `produk_kategori` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
