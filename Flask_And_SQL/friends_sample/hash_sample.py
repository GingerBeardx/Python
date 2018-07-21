import md5
password = 'nevermore'
hashed_password = md5.new(password).hexdigest()
print hashed_password