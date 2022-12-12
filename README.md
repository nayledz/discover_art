# discover_art
 'Discover Art' is a Django project, which was created for Python Web Framework courses at SoftUni.
 
This project gives you the opportunity to discover and buy original art from all around the world or sell your own art.
The application has the functionality to register user, edit and delete user’s profile, upload art for sale, buy art from other artists, search for paintings, delete and edit uploaded paintings, contact with the admins, check for order requests.  It has a public part, which is accessible by everyone and a private part, which is accessible only by authenticated users and admins. 

   This project is using PostgreSQL as a Database Service.
    
To implement the functionality the following models are used:
    
  -	model ArtUserManager;
  -	model ArtUser;
  -	model Account;
  -	model Product;
  -	model Order;
  -	model ArtContact.
  
The project app uses 3-rd party packages:
  -	django-crispy-forms;
  -	pillow;
  -	psycopg2.
