pam-mysql
=========

pam-mysql for CentOS 7 with sha256 support.

```
crypt (plain)

    The method to encrypt the user's password:

       0 (or "plain") = No encryption.  Passwords stored in plaintext.
                        HIGHLY DISCOURAGED.

       1 (or "Y")     = Use crypt(3) function.

       2 (or "mysql") = Use MySQL PASSWORD() function. It is possible
                        that the encryption function used by PAM-MySQL
                        is different from that of the MySQL server, as
                        PAM-MySQL uses the function defined in MySQL's
                        C-client API instead of using PASSWORD() SQL function
                        in the query.

       3 (or "md5")   = Use plain hex MD5.

       4 (or "sha1")  = Use plain hex SHA1.

       5 (or 'sha256')= Use plain hex SHA256.
```
