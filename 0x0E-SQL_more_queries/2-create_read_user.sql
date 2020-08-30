-- creates Database if not already exist and grants privileges to User
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
GRANT SELECT ON hbtn_0d_2.*
TO user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
FLUSH PRIVILEGES;
