USE [master]
GO
/****** Object:  Database [Definite]    Script Date: 15/6/2020 3:44:00 PM ******/
CREATE DATABASE [Definite]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'Definite', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL12.MSSQLSERVER\MSSQL\DATA\Definite.mdf' , SIZE = 4096KB , MAXSIZE = UNLIMITED, FILEGROWTH = 1024KB )
 LOG ON 
( NAME = N'Definite_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL12.MSSQLSERVER\MSSQL\DATA\Definite.ldf' , SIZE = 1024KB , MAXSIZE = 2048GB , FILEGROWTH = 10%)
GO
ALTER DATABASE [Definite] SET COMPATIBILITY_LEVEL = 120
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Definite].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [Definite] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [Definite] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [Definite] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [Definite] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [Definite] SET ARITHABORT OFF 
GO
ALTER DATABASE [Definite] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [Definite] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [Definite] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [Definite] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [Definite] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [Definite] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [Definite] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [Definite] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [Definite] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [Definite] SET  DISABLE_BROKER 
GO
ALTER DATABASE [Definite] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [Definite] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [Definite] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [Definite] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [Definite] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [Definite] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [Definite] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [Definite] SET RECOVERY FULL 
GO
ALTER DATABASE [Definite] SET  MULTI_USER 
GO
ALTER DATABASE [Definite] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [Definite] SET DB_CHAINING OFF 
GO
ALTER DATABASE [Definite] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [Definite] SET TARGET_RECOVERY_TIME = 0 SECONDS 
GO
ALTER DATABASE [Definite] SET DELAYED_DURABILITY = DISABLED 
GO
EXEC sys.sp_db_vardecimal_storage_format N'Definite', N'ON'
GO
USE [Definite]
GO
/****** Object:  Table [dbo].[customer_info]    Script Date: 15/6/2020 3:44:01 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[customer_info](
	[customer_id] [nchar](10) NULL,
	[customer_name] [nchar](10) NULL,
	[savingaccount] [nchar](50) NULL
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[transaction_info]    Script Date: 15/6/2020 3:44:01 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[transaction_info](
	[sender_id] [nchar](10) NULL,
	[receiver_id] [nchar](10) NULL,
	[transaction_date] [datetime] NULL,
	[amount_converted] [nchar](30) NULL,
	[currency_used_to_convert] [nchar](10) NULL,
	[amount_transacted_in_btc] [nchar](30) NULL
) ON [PRIMARY]

GO
INSERT [dbo].[customer_info] ([customer_id], [customer_name], [savingaccount]) VALUES (N'c123      ', N'Zephan    ', N'100000000                                         ')
INSERT [dbo].[customer_info] ([customer_id], [customer_name], [savingaccount]) VALUES (N'c321      ', N'Joel      ', N'100000000                                         ')
INSERT [dbo].[customer_info] ([customer_id], [customer_name], [savingaccount]) VALUES (N'c451      ', N'Russell   ', N'100000000                                         ')
INSERT [dbo].[customer_info] ([customer_id], [customer_name], [savingaccount]) VALUES (N'c654      ', N'Kar Wai   ', N'100000000                                         ')
USE [master]
GO
ALTER DATABASE [Definite] SET  READ_WRITE 
GO
