![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

<h1>Portfolio_Project_5 --- Ecommerce Project</h1>
<h1>The Airsoft Workshop</h1>

<p>The Idea for this website came from my hobby. I am an airsofter and it is my biggest passion outside work. I got really envolved in the sport and have always looked at the idea of working more closely within the airsoft community and would like to provide a unique, bespoke service that offers spray painting, camoflaging of Realistic Imitation Firearms (RIFs). When i speak with fellow airsofters they always would like a way to stand out from the crowd and have unique equipment and that is where the airsoft workshop comes into play. from selling consumables and to offering high-end services such as maintainance and repairs.</p>

click here to go to the deployed website: <a href="https://airsoft-workshop.herokuapp.com/" target="_blank"><b><i>"Airsoft Workshop"</i></b></a>
<!-- Change HREF HERE -->
<br><br>

![image](https://user-images.githubusercontent.com/72948843/205629357-1a4f2095-590a-47c1-b1c9-f8f89eba4c2f.png)

<br>

# Contents

* [**User Experience UX**](<#user-experience-ux>)
    * [User Stories](<#user-stories>)
    * [Epics](<#Epics>)
    * [Project Management](<#project-management>)
    * [Data Model](<#data-model>)
    * [Wireframes](<#wireframes>)
    * [Site Structure](<#site-structure>)
* [**Web Design & Stylings**](<#web-design-&-stylings>)
    * [ColourScheme](<#colour-scheme>)
    * [Fonts](<#fonts>)
* [**Features**](<#features>)
    * [Existing Features](<#existing-features>)
    * [Input Validation and Checking](<#input-validation-and-checking>)
    * [Future Features](<#future-features>)
* [**Testing**](<#testing>)
* [**SEO & Web Marketing**](<#seo-&-web-marketing>)
    * [SEO](<#seo>)
    * [Web Marketing](<#web-marketing>)
* [**Technologies Used**](<#technologies-used>)
* [**Libraries**](<#libraries>)
* [**Deployment**](<#deployment>)
    * [Creating a Database](<#creating-a-database>)
    * [Deployment of the project](<#deployment-of-the-project>)
    * [Cloning of the project](<#cloning-of-the-project>)
    * [Setting the email service](<#setting-the-email-service>)
* [**Credits**](<#credits>)
* [**Acknowledgements**](<#acknowledgements>)


<!-- new contents to be added to this list -->

# User Experience UX

## User Stories
User Stories make up an important part of the process to help steer the project in the right direction. These itemized points act as a guide during the build of the project.

Follow this link to <a href="https://github.com/GrantWils23/Portfolio-Project-5--Ecommerce-Applications/blob/main/assets/User%20Stories%20Spreadsheet.pdf" target="_blank"><b><i>"The User Stories List"</i></b></a>.

An additional User Story to be added on here is..... As a "User", I can "Add my favourite items to a list" So that "I can find them easily if I wish to purchase them when i return to the website."

[Back to Top](<#contents>)

<br>

## Epics
Epics Explaining what has been acheived

<!-- Display in form of a picture from the PDF within Excel file i created -->
[Back to Top](<#contents>)

## Project Management
To work along with the user stories that i created to help build the site, I used GitHubs's Project Board to manage my workflow. The Kanban style work board is very useful when trying to implement a working Agile environment. This tool helped me break down the importance of time management and helped me track my progress. It's a super powerful tool, with the abiltity to add small notes and labels to items within the project board.
<br>

![image](https://user-images.githubusercontent.com/72948843/200688676-60bbf45a-9a46-4b59-be1a-c8c9983a935d.png)
<br>

[Back to Top](<#contents>)
<br>

## Data Model
Here below you can find the Data schema used to create the data models. This was useful in helping me understand the flow and direction on how to create the app models, views and templates. The model was split into two sections, The Services Models and the Store models.

- Follow this link to <a href="https://github.com/GrantWils23/Portfolio-Project-5--Ecommerce-Applications/blob/main/assets/airsoft-workshop-database-schema-shopping-model.png" target="_blank"><b><i>"The Airsoft Workshop Database Schema Shopping Model"</i></b></a>.

- Follow this link to <a href="https://github.com/GrantWils23/Portfolio-Project-5--Ecommerce-Applications/blob/main/assets/airsoft-workshop-database-schema-services-model.png" target="_blank"><b><i>"The Airsoft Workshop Database Schema Services Model"</i></b></a>.

<br>

[Back to Top](<#contents>)

## Wireframes
The Wireframes for this project are the building foundations of the website. Some of the ideas have come from user feedback. Friends and fellow airsofters who would use a service like this gave me valuable information as time went on what works and what does not... These basic templates were the foundation of which the website style is built on but with the help of real user feedback I implemented it along the way.

Follow this link to <a href="https://github.com/GrantWils23/Portfolio-Project-5--Ecommerce-Applications/blob/main/assets/Airsoft%20Workshop%20Wireframes.pdf" target="_blank"><b><i>"The Airsoft Workshop Wireframes"</i></b></a>.


[Back to Top](<#contents>)
<br>
 
 ## Site Structure
Navigating around the site is easy due to the simple layout. here below is the basic site structure. <!-- template from old project - edit accordingly -->
<ul>
    <li>Home Page</li>
    <li>Services Page</li>
    <li>Store</li>
    <li>Tech Services</li>
    <li>Paint Services</li>
    <li>Allauth Pages (includes Login, Logout, Register, etc...)</li>
    <li>My Profile</li>
    <li>Product Management (includes search filters and add views)</li>
    <li>Products</li>
    <li>Product Details</li>
    <li>Bag</li>
    <li>Checkout</li>
    <li>About Us</li>
    <li>Contact Us</li>
    <li>Privacy Policy</li>
    <li>Sitemap</li>
</ul>

The Desktop version of the site is very spacious but when the user drops down to a smaller aspect ratio the content will be forced to occupy a majority of the screen not to waste the restricted space that is left on the display. This will greatly improve the UX as it will be easier to use on smaller devices, just as it would be on a desktop or larger screen device.

[Back to Top](<#contents>)
<br>

# Web Design & Stylings

To speed up the process of making a really interactive website page, I learnt to use Bootstrap to its full capability to help design an aesthetically pleasing website that and then created custom details to the brands design to give it a unique appeal and enhance the UX. by using bootstrap, I have access to working, proven code that has help build an offcanvas menu bar, cards, toasts and footers. and it allows me to spend more time on the core structure of the website in the logic and how the site should operate. below are some specification detailng the other design aspects of the website...

## Colour Scheme
the colour scheme chosen for this website is a submersive navy-blue/black colour and dark grey  <!-- colour tags go here -->. This is really nice as it highlights images and makes reading easy as a light grey font was chosen to work in contrast with the background color.

The colour scheme also around the website largely uses hints of green throughout to add the unique personal touch of the Airsoft Workshop website. 

- The main logo font is green, it naturally appears throughout the website to give the user an enhanced UX.

- The homepage "GEAR UP" button is really important to the website: Its unique to all the other buttons on the site as it is designed to draw the user in. It holds the same color tones that feature throughout the site.	

- Functional buttons within the website use all of the bootstraps inbuilt buttons. The green success button features mostly thoughout the site as a button to navigate and make progressive page changes. The secondary button also appears in the site which serves a majority of the time in the site as a return button.

The colour codes are:
- Custom green: #198754
- Main background colour: #222
- Font color against the Black-Grey background: #ffffff8c 
- background for Navbar and Footer: #212529
- font-color against Navbar and Footer background: #6c757d

Main Logo Colour:
<br>

![image](https://user-images.githubusercontent.com/72948843/200686879-b5c220a3-6222-46d4-b014-56d0dc7160ad.png)

Font colours against background in Footer:
<br>

![image](https://user-images.githubusercontent.com/72948843/200686372-3eb0c765-8861-4f4d-a2ec-1a14aa2363cf.png)

Home page "Gear Up" button static:
<br>

![image](https://user-images.githubusercontent.com/72948843/200687036-14320df6-200d-428d-9932-6d28680daea2.png)

Home page "Gear Up" button on hover:
<br>

![image](https://user-images.githubusercontent.com/72948843/200686487-b362fa7d-6b35-49bb-8365-c254f7e02c56.png)


<br>

[Back to Top](<#contents>)
<br>

## Fonts

The selections of the fonts were chosen really carefully, the main logo font used is "Special Elite" which was supplied from Google Fonts. This font was chosen for its unique 'worn' style that gives it a ruggedness and slight military look. The secondary font used is 'Marcellus,' which too can be found on Google Fonts. A third font has been used a in the site to give a better reading experience on the dark background 'GFS Didot'.

The first font...
<br>

![image](https://user-images.githubusercontent.com/72948843/200687580-6dd232c4-c40c-461b-af68-701420cffdbe.png)

The second font...
<br>

![image](https://user-images.githubusercontent.com/72948843/200688308-ec471f6e-8714-4e65-8880-865be57c98fe.png)
<br>

The tertiary font...
![image](https://user-images.githubusercontent.com/72948843/204630491-c58bc122-55c7-43e4-b38b-297ddd660f93.png)
<br>

[Back to Top](<#contents>)
<br>

# Features

## Existing Features
* [Navigation Menu](<#navigation-menu>)
* [Allauth Functionality](<#allauth-functionality>)
* [services Page](<#services-page>)
* [Tech Services](<#tech-services>)
* [Paint Services](<#paint-services>)
* [Store](<#store>)
* [Basket](<#basket>)
* [Checkout](<#checkout>)
* [Footer](<#footer>)
* [Toast and Messages](<#toast-and-messages>)
* [Wishlist and User Profile](<#wishlist-and-user-profile>)
* [Admin Controls](<#admin-controls>)



## Navigation Menu
<!-- examples form previous, change accordingly -->
- The nav menu is set at the top of all the pages. It is fully responsive and converts to a small dropdown menu on smaller screen ratios for a better UX. The nav contains links to all the important customer usable pages.
- The nav menu is fitted inside of a clickable button that opens up a offcanvas dropdown menu. It is hidden off screen to increase the viewing portal space around giving the user more space and a less cultered view.
- The offcanvas menu has link to the homepage, to the services page and then links to all the individual service links, along with the account dropdown menu with all related field options contained within.
- The logo is clickable with a link back to the home page for enhanced UX.
<br>
<br>

![image](https://user-images.githubusercontent.com/72948843/200792615-30d89016-b13e-4193-a272-af9e689ca7cf.png)
<i>Navbar menu - smaller aspect ratio devices</i>

![image](https://user-images.githubusercontent.com/72948843/200794557-5d6fc4d2-cff6-4396-aa50-9433cb7a38e7.png)
<i>Off Canvas Dropdown menu</i>

![image](https://user-images.githubusercontent.com/72948843/200793688-14d6f2c0-57e5-43a7-9b9c-f30ed583b5b8.png)
<i>Store sub category options</i>

![image](https://user-images.githubusercontent.com/72948843/200795018-60aed44b-8229-41df-a1f0-ad74e9f97c1c.png)
<i>Account Dropdown menu - Superuser View</i>

[Back to Existing Features](<#existing-features>)
<br>

## Allauth Functionality
<!-- example text from pervious project, change accordingly -->
- The allauth functionality allows the generation of user profiles which helps customers create a profile that they can save and have records of their orders in their account. This has been intergrated within the airsoft workshop to give the user the ability to signin, signout, register.

![image](https://user-images.githubusercontent.com/72948843/200797736-de2a378e-5bca-4fd7-a2c5-8e64563b5541.png)
<i>Sign in</i>

![image](https://user-images.githubusercontent.com/72948843/200797938-24af6e58-4d31-4ec6-b0e5-9c46956c8c91.png)
<i>Sign Up</i>

![image](https://user-images.githubusercontent.com/72948843/200798310-00f5843d-3883-4b8f-89cd-511e2953a7c0.png)
<i>Sign Out</i>
<br>

[Back to Existing Features](<#existing-features>)
<br>
<br>

## Services Page
The services page is designed to give the users a brief insight into the services of what the company offers its clients with a description of the beautician’s experience and really is where you get a feel for the company and the professional nature of it. The page is designed to be eye-catching and give the user a well-rounded experience as they view what company has to offer. The cards have a green shadow appear around them when the cursor enters a card to focus your view on the card the user are reading helping to boost the users UX.
 
![image](https://user-images.githubusercontent.com/72948843/200798942-5810353e-1a85-45bc-bb6b-deb8c7594b5d.png)
<i>Services page on a large view device</i>


![image](https://user-images.githubusercontent.com/72948843/200799508-1c5b11b1-2eb0-4190-91e8-e08138a090c4.png)
<i>Services page on a small view device</i>

![image](https://user-images.githubusercontent.com/72948843/204614385-066b085d-0cdc-432c-91d2-3530e2f20fa3.png)
<li>Services page modal</li>


[Back to Existing Features](<#existing-features>)
<br>

## Tech Services
<br>
The Tech services page is user friendly and is very clear to read, Its high contrast background on the hover over the radio select buttons images make a great visual indicator to on hovered items, which enhances the user's experience on the page.

![image](https://user-images.githubusercontent.com/72948843/204584418-08a60b02-d0a1-4eaf-95b1-9524ddd4db33.png)

<!-- Add later more content -->

[Back to Existing Features](<#existing-features>)
<br>


## Paint Services
<br>

The Paint services page is user friendly and is very clear to read, Its high contrast background on the hover over the radio select buttons images make a great visual indicator to on hovered items, which enhances the user's experience on the page.
<br>
The radio buttons in the form have images attached to them help. The images are of the paint job the user can choose from if he wishes to paint his RIF. This clear display helps the user commit to a style he is picking. This approach is far better than a text based select box which wouldn't provide thec user with a lot of information, again adding to the user experience.

![image](https://user-images.githubusercontent.com/72948843/204585034-758387cd-23c9-40c5-ad04-44f78330f48f.png)

<!-- Add later more content -->

[Back to Existing Features](<#existing-features>)
<br>

## Store
<br>

![image](https://user-images.githubusercontent.com/72948843/204611307-f5b40c2b-ffde-4414-9c7e-3a5b2e89d196.png)
- Desktop View

![image](https://user-images.githubusercontent.com/72948843/204613256-9ce42b07-3566-4cfd-9d26-594fb0ee9c5d.png)
- Mobile View

## Basket
<br>
<!-- Add later more content -->

![image](https://user-images.githubusercontent.com/72948843/204585310-78828b14-fb87-4131-82de-3ae474475491.png)
- Desktop view

![image](https://user-images.githubusercontent.com/72948843/204585420-56df2ba8-ecbf-4ef6-ab5b-3f9b495c54dd.png)
- Mobile view

[Back to Existing Features](<#existing-features>)
<br>


## Checkout
<br>
<!-- Add later more content -->
The checkout view informs the user of all the criteria required to complete the purchase, along with a small recap window of what the user is ordering.

Upon completion of an order, a confirmation email and are redirected to a success page where you can review your purchase and are prompted to head back into the store.

![image](https://user-images.githubusercontent.com/72948843/204585782-f752ae1c-537b-4c4f-b134-1693e7ebfdb0.png)
- Desktop view

![image](https://user-images.githubusercontent.com/72948843/204617450-e889899d-f006-4141-80e0-ef3186fc5a3c.png)
- Checkout Success
<br>


[Back to Existing Features](<#existing-features>)
<br>

## Footer
The footer contains all the main menu links but also some addition links that are to extra content in the shape of Contact_us, About_us, FAQs, Sitemap, Privacy Policy. These additional links are important to the site but in general do not need to be present in the main navbar as they are less likely to be visited. Beyond these links are some extra content too. We have a Subscribe to Newsletter housed in footer, for those who wish to join our email marketing to recieve monthly updates and promo codes. Also beneath a line break we have a copyright disclaimer and social media links and other important links related to the company.

- The Subscribe to newsletter feature is located in the footer so that it doesn't intefer with the Hero Image in the main view and for new potential customers they have a quick and easy means of signing up to our email marketing scheme.
 
![image](https://user-images.githubusercontent.com/72948843/204583684-b7b53cf5-f524-4358-977b-39a9dc0170f7.png)
<i>Footer on a large view device</i>


![image](https://user-images.githubusercontent.com/72948843/204584030-4cda3fe8-c432-461f-9fdc-0e1f47fc4322.png)
<i>Footer on a small view device</i>
<br>

[Back to Existing Features](<#existing-features>)
<br>

## Toast and Messages
<br>
The toast and messaging system gives really helpful feedback to the user in realtime on when an action is performed. Below are some examples of what the messaging system looks like. toast have a glow indicating the level of message and its importance to the user.

![image](https://user-images.githubusercontent.com/72948843/204586060-1524852a-da6e-425e-b105-fe29808cf1ce.png)
- success


![image](https://user-images.githubusercontent.com/72948843/204583113-f2cbbf8b-312d-46ca-86c8-77206890b77a.png)
- info


![image](https://user-images.githubusercontent.com/72948843/204582620-03d3e184-4c90-45e2-a94a-88ec6b086ef5.png)
- warning


![image](https://user-images.githubusercontent.com/72948843/204583319-f92db3b8-fe05-47d2-808a-4556ea4188f8.png)
- error


[Back to Existing Features](<#existing-features>)
<br>


## Wishlist and User Profile
<br>

The website boasts a user profile panel and registered users have access to a multiple abilities in which they can manage their account details, reset passwords and user details. The page also has a wishlist display where users can track their favorite items or items they wish to purchase a later date.

![image](https://user-images.githubusercontent.com/72948843/204586686-0372ab26-b1e7-4817-b322-dcc75f9bbba9.png)

![image](https://user-images.githubusercontent.com/72948843/204586830-a656053b-b068-4f3b-955d-9f4e20b802d4.png)

![image](https://user-images.githubusercontent.com/72948843/204587086-70982166-ce19-4e3b-982b-74656b72faa0.png)

[Back to Existing Features](<#existing-features>)
<br>


## Admin Controls
<br>
<!-- Add later more content -->

The Admin Controls are where the store owner has additional functionality outside a normal registered user. here the admin has control on product management. This can be navigated to via the offscreen canvas dropdown menu and via the footer, for easy of access. The admin views contains a tracking orders system where they can check orders placed and form submissions regarding the requested paint jobs and tech works. also the admin can add more products and related product details. Also additional new delivery methods can be added to the store, if the store admin wishes to add at a later date.

- Admin Control Panel

![image](https://user-images.githubusercontent.com/72948843/205621092-b00d59d5-67b6-43cb-92aa-e8541d9ddac2.png)
<br>

- Admin orders display

![image](https://user-images.githubusercontent.com/72948843/204621052-41277821-7a00-49d1-9cf0-6d5bf49cf755.png)
<br>

- Admin Paint Quotes display

![image](https://user-images.githubusercontent.com/72948843/204622361-d970b22a-8088-45fb-ba77-3f23334b2c49.png)
<br>

- Add products page

![image](https://user-images.githubusercontent.com/72948843/205621285-95b28285-86e7-419c-9242-21a2e9846142.png)
<br>

- Delete pop-up alert

![image](https://user-images.githubusercontent.com/72948843/204655356-5173c49a-1920-46fe-b55b-0b83e5c7fe19.png)
<br>
<br>
<br>

[Back to Existing Features](<#existing-features>)
<br>


<br>
<br>
<br>

## Input Validation and checking
<!-- template from old project, change accordingly -->
Validation of the form is implemented by checking before the document is submitted is valid to submit. This is achieved by multiple methods:
<ul>
    <li>To validate the phone number being entered into the form, django-phonenumber-field was used. It checks the input to see if it is a valid phone number and returns an error message if it is not valid upon submission. This inbuild validation was used on the profile, tech and paint services models but not the Order Model.
    </li>
    <li>To validate the country field, django-countries were used. It checks whether the data entered into the field is entered correctly.</li>
</ul>
Using all the inbuild form validations helped create quick clean code without having to write many custom form validations.

Incorrect data validations:

![image](https://user-images.githubusercontent.com/72948843/204623185-83b4fec9-9590-434b-8782-075cbe5569e8.png)
![image](https://user-images.githubusercontent.com/72948843/205713769-ea7e0e52-2adc-48ba-8c2e-cc125b4a0796.png)
![image](https://user-images.githubusercontent.com/72948843/205713826-c36fcd4c-f741-4a4e-850c-3e0318dc3e7b.png)
![image](https://user-images.githubusercontent.com/72948843/205713921-76eb0997-1774-4abf-af88-26a52235a379.png)

Incorrect card details validation:

![image](https://user-images.githubusercontent.com/72948843/204623529-64001769-df3a-4572-a7a5-6842e1315073.png)

Missing field upon submitting validation:

![image](https://user-images.githubusercontent.com/72948843/204623756-90d46dae-ab10-4f8c-9967-9b8235ceedc6.png)

[Back to Top](<#contents>)

<br>

## Future Features
<br>
There are some additional features that could be implemented at a later date. We have some new user stories below which express some ideas on how to make the site better:

-  Users have expressed a desire to leave comments on products and to be able to rate the products themselves. This would give the customers more product feedback on the quality of the products on sale.

- Users have also expressed an interest in a more robust platform regarding paint and tech services. Similar to the above feature, a register user can leave feedback on jobs done and comment in the form of some sort of job review blog. This would give future customers more power in decision-making on the reliability of the work the company offers in the tech and painting sector.

Some future user stories are detailed below:

- As a "store Owner", I can "tick orders off as completed, shipped, cancelled or pending", so that "I can manage the status of any given order in the database."

- As a "Registered customer", I can "track the status of my order", so that "I know when I can expect it to arrive."

[Back to Top](<#contents>)
<br>
<br>
<br>

# Testing

<p>To find out more about the tests related to the project. please follow this <a href="https://github.com/GrantWils23/Portfolio-Project-5--Ecommerce-Applications/blob/main/tests/TESTS.md" target="_blank">link</a> to the testing page.</p>

[Back to Top](<#contents>)
<br>
<br>
<br>

# SEO & Web Marketing

## Search Engine Optimization

To aid the reliability of the websites success, search engine optimization practices where implemented in the wesite to try and boost its raitings on a search.
To do this, I brainstormed criteria based on the three key unique selling points of the company, two of which are specialization in services. I tried to identify those pointwebsite'splement it into the site structure where appliwere by using the meta tawebsitethe header and using keywords and descriptions to boost its chances of being found in a search result.

Follow this link to the documentation created for <a href="https://github.com/GrantWils23/Portfolio-Project-5--Ecommerce-Applications/blob/main/assets/seo-research-documentation.pdf" target="_blank"><b><i>" keyword research"</i></b></a>.

<!--  -->

[Back to Top](<#contents>)

<br>

## Web Marketing
* [Social Media Marketing](<#social-media-marketing>)
* [Allauth Functionality](<#email-marketing>)

[Back to Top](<#contents>)

### Social Media Marketing

As part of the company's approach to increase brand awareness, web marketing is an important part of the companies brand presence. Airsoft is a very close community sport and word of mouth goes a long way to generating brand confidence. Using web organic marketing techniques

To create the page.. you need to log in and create a new page.

![image](https://user-images.githubusercontent.com/72948843/205505248-1960a1b9-f2dc-4a72-9fab-0780e1b03187.png)

Next, we need to add more information about our company including the website, address, telephone number and opening times.

![image](https://user-images.githubusercontent.com/72948843/205505886-5d8e70a3-a821-4a86-af1d-0f1cd0d3d908.png)

Next, to comply with facebooks strict compliances in regards to advertizing firearms, even though they are not real, i have opted to change the background picturee something less intimidating. the image chosen is of a firing range, which ties in with one of the three themes of the company. The "Tech Service" side, whereby once a RIF is repaired, it would be checked down range to check how it performs post works.

![image](https://user-images.githubusercontent.com/72948843/205507503-9a739639-9557-412c-b123-ff232093d2c2.png)

Moving forward, you can choose to connect whatsapp to the page, but I skipped this part. after that you can choose to invite friends to the website. I started by inviting people who i know would be interested in this ecommerce store.

![image](https://user-images.githubusercontent.com/72948843/205507882-403d7f6e-706c-4376-bac2-fd76edf83752.png)

Finally, the last step is to inform the users to stay informed regarding information from this page. I selected both options and finalised my Facebook page.

![image](https://user-images.githubusercontent.com/72948843/205508019-2bdb44e0-0e27-45e1-95cc-d5f4078f890e.png)

Now with that done, the page is complete... a popup will appear and you can take a tour on how to create a post...

![image](https://user-images.githubusercontent.com/72948843/205508246-90640bba-22d4-46e4-8519-59bff054ef75.png)

Below you can see the first post created for the Airsoft Workshop!

![image](https://user-images.githubusercontent.com/72948843/205509133-056403c2-2ad0-4ecf-874a-f03c44e45bb8.png)

lastly but not least, we need to add the pages to the facebook links within our website, so anywhere with an ```<a></a> ``` tag linked to facebook needs our Facebook page link added directly to it.

![image](https://user-images.githubusercontent.com/72948843/205509648-7574c2ad-e703-4f5a-93fc-19ccd36739e8.png)

To generate a larger awareness of our social media presence, I added a larger link to our facebook page so that it attracts the eye of any visiting site users.

![image](https://user-images.githubusercontent.com/72948843/205509961-8ea9e613-b7a0-483f-a166-55eca4607033.png)

[Back to Top](<#web-marketing>)

<hr>

### Email Marketing

Next We want to take advantage of email marketing to boost brand awareness of the company. To do this, I used mailchimp. so firstly i created an account and once that has been set up I can show below how Email marketing was employed in this website.

click on the create button on the left of the dropdown menu.

![image](https://user-images.githubusercontent.com/72948843/205510647-f0950de2-73c3-4dbd-b016-623dbe033793.png)

first in the menu you will see a list of options... click on the email link in the menu.

![image](https://user-images.githubusercontent.com/72948843/205510697-07b56f52-914a-4f6f-9d7f-ae849650c1cc.png)

now for Airsoft Workshop, I have already designed my footer in mind with a place to have an embedded sign up form... so I will select the embedded form option of the three.

![image](https://user-images.githubusercontent.com/72948843/205510574-f25b8f0e-2f21-47b8-9463-bce73ce20c3e.png)

with the first step, it gives us a list of options of what we wish to add to this embedded form. I only want the email address, so i just progressed to the next step.

![image](https://user-images.githubusercontent.com/72948843/205511032-3390eff6-3b40-4556-ba5d-f110f52ff0c8.png)

Now the form is ready... I can copy this code and add it to the footer of our website. it contains some javascript so we will need to add this code in the js script tags in the base.html of our website too.

![image](https://user-images.githubusercontent.com/72948843/205511156-21778c5f-f331-40f2-a5bd-cb1cbde92766.png)

with this code, you can now implement it and style it how you wish, after some CSS alterations this is how my final embedded form looks...

![image](https://user-images.githubusercontent.com/72948843/205519068-0048a022-0d26-4673-b0b9-ec4a382b2970.png)

just a quick check to see if it worked... I'll go to Mailchimp and check if my test email address went through...

![image](https://user-images.githubusercontent.com/72948843/205519366-662230c5-f455-4ec2-a379-214333979960.png)

Yes, success. After sending a fake email via the form, I can see the email address has been added to my list of contacts. From here, as the business grows and more people sign up, Airsoft Workshop can target the interested potential customers with special offers or newsletters to try and grab their attention and encourage sales.

<!-- Display in form of a picture from the PDF within Excel file i created -->

[Back to Top](<#web-marketing>)


## Technologies Used
<!-- will need updating, template from previous project, check at end against requirements.txt -->
<li><a href="https://github.com/" target="_blank">GitHub</a> -The site was used to edit and host the website.</li>
<li><a href="https://gitpod.io/projects" target="_blank">GitPod</a> - Used in the deployment and creating the website.</li>
<li><a href="https://git-scm.com/" target="_blank">GitBash</a> - Used for committing and pushing files to github in the terminal through version control. GitBash - Terminal used to push changes to the GitHub repository.</li>
<li><a href="https://www.python.org/" target="_blank">Python</a> - This was used in the production to get the game running as it is required for the app to run.</li>
<li><a href="https://www.djangoproject.com/" target="_blank">Django</a> - The Django web Framework was used to create the app and maintain it.</li>
<li><a href="https://psycopg.com" target="_blank">Psycopg</a> - The database with which the app runs are PostrgeSQL.</li>
<li><a href="http://pep8online.com/" target="_blank">pep8online</a> - This site was used to validate the python code to check for any errors within my writing.</li>
<li><a href="https://www.heroku.com/" target="_blank">Heroku</a> - This was used to deploy the website online for users to see and active site.</li>
<li><a href="https://www.elephantsql.com/" target="_blank">ElephantSQL</a> - This free online database provider was used to host the website's database.</li>

<li><a href="https://pypi.org/project/django-phonenumber-field/" target="_blank">Django-phonenumber-field</a> -Is a django module used for validating a phonenumber that is to be stored into the database.</li>
<li><a href="https://django-allauth.readthedocs.io/en/latest/" target="_blank">Django-allauth</a> - Is an authentication app that is used to check validity of the users accessing the website.</li>
<li><a href="https://django-crispy-forms.readthedocs.io/en/latest/" target="_blank">Django-crispy-forms</a> - Is a form generator helper that enables quick and tidy forms to be made with minimal input on the front end.</li>
<li><a href="https://fontawesome.com/" target="_blank">fontawesome</a> - Is used to get the icons at the bottom of the page for the social media resources.</li>
<li><a href="https://favicon.io/" target="_blank">Favicon</a> - was used to design the Favicon for display in the browser tab</li>
<li><a href="https://www.flaticon.com/" target="_blank">Flaticon</a> - Was used to get free style icon for displaying in the services form</li>

<li><a href="https://getbootstrap.com/" target="_blank"> Bootstrap </a> - Bootstrap was used in this project to help create the website with fast and easy web designs, from drop in code for modals, nav bars and how the viewports react.</li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS" target="_blank"> CSS </a> - Aside from some basic stylings inherited from bootstrap, CSS was used to customise the website to a tailored fit. The design schema was heavily influenced by the theme and colours requested and the wireframes used at the beginning stage of development. CSS gave the ability to create a beautiful website exactly as the client requested.</li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTML" target="_blank"> HTML </a> - HTML used as the language to render the text in the front-end.</li>
<li><a href="https://www.pexels.com/" target="_blank"> Pexels </a> - An online stock of photos that are royalty free to use.</li>
<li><a href="https://www.istockphoto.com/" target="_blank"> IstockPhotos </a> - An online store of photos that have to be purchased in order to use on the deployed web.</li>
<li><a href="https://docs.djangoproject.com/en/4.0/topics/email/" target="_blank"> Django Email </a> -  Django Email is a very useful and powerful tool that allowed the clients to receive emails regarding their booking. It is a really useful tool that provides real time functionality with great results.</li>
<li><a href="https://compressor.io/" target="_blank"> Compressor </a> -An online compressing tool, great for compressing stock images down to a user friendly size, and it is completely free to use.</li>
<li><a href="http://pep8online.com/" target="_blank"> PEP8 Validator </a> - An online website used to validate my Python code</li>
<li><a href="https://jshint.com/" target="_blank"> JSHint Valdiator </a> - An online website used to validate my JavaScript code</li>
<li><a href="https://validator.w3.org/nu/" target="_blank"> HTML Validator </a> - An online website used to validate my HTML code.</li>
<li><a href="https://jigsaw.w3.org/css-validator/" target="_blank"> CSS Validator </a> - An online website used to validate my CSS code.</li>
<li><a href="https://developer.chrome.com/docs/devtools/" target="_blank"> Google Chrome DevTools </a> - An online resource that lays within Google Chrome used to debug the website during development.</li>
<li><a href="https://drawsql.app/" target="_blank"> DrawSQL </a> - An online app used to create the database schema.</li>
<li><a href="https://color.a11y.com/" target="_blank">A11y</a> - An online accessibility validator that checks the colour of the background against the text.</li>
<li><a href="https://stripe.com/gb" target="_blank">stripe</a> - A secure payment app used to recieve payments.</li>
<li><a href="https://miniwebtool.com/django-secret-key-generator/">MiniWebTools</a> - Used to create a random Django secret key for my project in Heroku</li>
<li><a href="https://temp-mail.org/">Temp-Mail</a> - A Handy tool that was used to create fake accounts to perform checks on email functionality during the deployed development stage.</li>
<li><a href="https://www.xml-sitemaps.com/">XML-sitemaps</a> - A free sitemap generator the sitemap for my the website</li>
<li><a href="https://www.privacypolicygenerator.info/">Privacy Policy Generator</a> - A free privacy-policy generator that I used for the deployed heroku website</li>
<li><a href="https://www.facebook.com/">Facebook</a> - I used Facebook to create an online marketing presence to advertise the company on to Facebook users who follow the Companies activities and who are interested in airsoft.</li>
<li><a href="https://mailchimp.com/">Mailchimp</a> - Mailchimp is a email marketing device, used to help generate business by getting people to signup to newsletters and get information regarding the companies latest offers</li>
<br>

[Back to Top](<#contents>)
<br>

## Libraries
<!-- will need updating, template from previous project, check at the nd against requirements.txt -->
<p>The libraries used in this project are located in the requirements.txt file and were set up in the virtual environment to get the project working. Below is the list of libraries used to run the website:</p>

<ul>
    <li><a href="https://pypi.org/project/asgiref/" target="_blank">asgiref</a> -  Reference ASGI adapters and channel layers.</li>
    <li><a href="https://pypi.org/project/backports.zoneinfo/" target="_blank">backport.zoneinfo</a> - The module used to implement the IANA time zone database in the python standard libary.</li>
    <li><a href="https://pypi.org/project/Babel/" target="_blank">Babel</a> - A collection of tools for internationalizing Python applications.</li>
    <li><a href="https://pypi.org/project/boto3/" target="_blank">boto3</a> - Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python, which allows Python developers to write software that makes use of services like Amazon S3 and Amazon EC2..</li>
    <li><a href="https://pypi.org/project/botocore/" target="_blank">botocore</a> - A low-level interface to a growing number of Amazon Web Services. The botocore package is the foundation for the AWS CLI as well as boto3.</li>
    <li><a href="" target="_blank">crispy-bootstrap5</a> - A collection of tools for internationalizing Python applications.</li>
    <!-- <li><a href="https://pypi.org/project/click8/" target="_blank">click</a> - A python package to help write command line interfaces with as little code as necessary.</li> -->
    <!-- <li><a href="https://pypi.org/project/coverage/" target="_blank">coverage</a> -  A python package that helps determine test coverage.</li> -->
    <li><a href="https://pypi.org/project/dj-database-url/" target="_blank">dj-database-url</a> - This utility package allows the user to utilize the "DATABASE_URL" environmental variable to configure the Django App.</li>
    <li><a href="https://pypi.org/project/Django/" target="_blank">Django</a> - A high-level Python web framework that encourages rapid development and clean, pragmatic design.</li>
    <li><a href="https://pypi.org/project/django-allauth/" target="_blank">django-allauth</a> - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.</li>
    <li><a href="https://pypi.org/project/django-countries/" target="_blank">django-countries</a> - A Django library that provides a country field out the box which is user friendly.</li>
    <li><a href="https://pypi.org/project/django-crispy-forms/" target="_blank">django-crispy-forms</a> -Build programmatic reusable layouts out of components, having full control of the rendered HTML without writing HTML in templates.</li>
    <li><a href="https://pypi.org/project/django-filter/" target="_blank">django-filter</a> - Django-filter is a reusable Django application for allowing users to filter querysets dynamically.</li>
    <li><a href="https://pypi.org/project/django-phonenumber-field/" target="_blank">django-phonenumber-field</a> - A Django library which interfaces with python-phonenumbers to validate, pretty print and convert phone numbers.</li>
    <li><a href="https://pypi.org/project/django-storages/" target="_blank">django-storages</a> - django-storages is a project to provide a variety of storage backends in a single library.</li>
    <li><a href="https://pypi.org/project/docutils/" target="_blank">docutils</a> - Docutils is a modular system for processing documentation into useful formats, such as HTML, XML, and LaTeX. For input Docutils supports reStructuredText, an easy-to-read, what-you-see-is-what-you-get plaintext markup syntax.</li>
    <li><a href="https://pypi.org/project/gunicorn/" target="_blank">gunicorn</a> - Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX.</li>
    <li><a href="https://pypi.org/project/jmespath/" target="_blank">jmespath</a> - JMESPath (pronounced “james path”) allows you to declaratively specify how to extract elements from a JSON document.</li>
    <li><a href="https://pypi.org/project/oauthlib/" target="_blank">oauthlib</a> - A generic, spec-compliant, thorough implementation of the OAuth request-signing logic.</li>
    <li><a href="https://pypi.org/project/phonenumberslite/" target="_blank">phonenumberslite</a> - This is a Python port of Google's libphonenumber library It supports Python 2.5-2.7 and Python 3.x (in the same codebase, with no 2to3 conversion needed)</li>
    <li><a href="https://pypi.org/project/Pillow/" target="_blank">Pillow</a> - Pillow is the friendly PIL fork by Alex Clark and Contributors. PIL is the Python Imaging Library by Fredrik Lundh and Contributors. As of 2019, Pillow development is supported by Tidelift.</li>
    <li><a href="https://pypi.org/project/psycopg/" target="_blank">psycopg2</a> - PostgreSQL database adapter for Python.</li>
    <li><a href="https://pypi.org/project/PyJWT/" target="_blank">pyJWT</a> - JSON Web Token implementation in Python.</li>
    <li><a href="https://pypi.org/project/stripe/" target="_blank">stripe</a> - A secure payment app.</li>
    <li><a href="https://pypi.org/project/python-dateutil/" target="_blank">python-dateutil</a> - The dateutil module provides powerful extensions to the standard datetime module, available in Python.</li>
    <li><a href="https://pypi.org/project/pylint-plugin-utils/" target="_blank">pylint_plugin-utils</a> - Utilities and helpers for writing Pylint plugins.</li>
    <!-- <li><a href="https://pypi.org/project/pytest/" target="_blank">pytest</a> - A simple, powerful testing package in python.</li> -->
    <li><a href="https://pypi.org/project/python-openid3/" target="_blank">python3-openid</a> - OpenID support for servers and consumers. Python 3 support fork.</li>
    <li><a href="https://pypi.org/project/pytz/" target="_blank">pytz</a> - World timezone definitions, modern and historical.</li>
    <li><a href="https://pypi.org/project/s3transfer/" target="_blank">s3transfer</a> - S3transfer is a Python library for managing Amazon S3 transfers. This project is maintained and published by Amazon Web Services.</li>
    <li><a href="https://pypi.org/project/requests-oauthlib/" target="_blank">request-oauthlib</a> - OAuthlib authentication support for Requests.</li>
    <li><a href="https://pypi.org/project/sqlparse/" target="_blank">sqlparse</a> - A non-validating SQL parser.</li>
    <li><a href="https://pypi.org/project/stripe/" target="_blank">stripe</a> - A Python library for Stripe’s API.</li>
    <li><a href="https://pypi.org/project/urllib3/" target="_blank">urllib3</a> - urllib3 is a powerful, user-friendly HTTP client for Python. Much of the Python ecosystem already uses urllib3 and you should too. urllib3 brings many critical features that are missing from the Python standard libraries:</li>

</ul>

<br>

[Back to Top](<#contents>)
<br>
<br>
<br>
<hr>
<br>
<br>
<br>

# Deployment

<!-- Update as I go -->

## Creating a Database
<p> for this part, I used <a href="https://www.elephantsql.com/" target="_blank">ElephantSQL</a> as it is a wonderful free service to use as long as our database is not too large. To set this up, please follow the steps below:</p>

1) Sign Up and make an account. (You will need to povide some card details but that will not be charged providing you dont exceed any limits).
![image](https://user-images.githubusercontent.com/72948843/204639943-93638333-43cd-453f-ae02-48f1ac6cccc3.png)

2) Upon completion of registration, you should be able to log in and get to the instance hompage, Here  in the right corner at the top of the screen (were in green), you will see your name and just beneath it a button that says "Create Instance" press it build a database.  
![image](https://user-images.githubusercontent.com/72948843/204640503-91b6d68f-3db2-4670-a96a-670770d62d0b.png) 

3) You have four steps to create the database, you need to fill out the name of which you want to give for this database and select the free turtle plan. (the tags are optional) Proceed to select region...
![image](https://user-images.githubusercontent.com/72948843/204641312-4e84fd98-7b63-434a-af3e-60c1098673ea.png)

4) Select a region and data centre that best suits your needs and go forward to the next page. The third step should skip as long as you haven't selected the paid service. Go ahead and create the database by confirming in the last step.
![image](https://user-images.githubusercontent.com/72948843/204643640-946d6324-456b-4d8a-bdeb-234062ddfcb9.png)
![image](https://user-images.githubusercontent.com/72948843/204644926-2f99e379-02a7-4e07-a50d-f0ec2fc747b4.png)

5) Now that is completed, you will be redirected to the instance page.
![image](https://user-images.githubusercontent.com/72948843/204643213-fc3ec90d-a82b-4ae1-a705-857da5a204ee.png)

6) Select your new database and it will take you to the panel where you can now see a link to your database's new URL. Copy this URL and you can now assign this to your environmental variables in either your env.py file or in Heroku as ```DATSBASE_URL```
![image](https://user-images.githubusercontent.com/72948843/204643640-946d6324-456b-4d8a-bdeb-234062ddfcb9.png)

<br>
<br>
<br>
<hr>
<br>
<br>

## Deployment of the project

### Deployment to Heroku
<p>To deploy the site is a labour intensive process. follow the steps below for a stress free deployment:</p>

First and foremost, if you are not a user of Heroku, sign up to its services, once you are logged in, in the top right corner there is a button "New". Click on the button and then click on "create new app".

![image](https://user-images.githubusercontent.com/72948843/182254035-7a6d430b-10bb-4adb-acda-fe21e2a2cd8e.png)
 
Once the page loads, it asks you to put in an app name and your preferred region. I choose Europe as it is my current region.
 
![image](https://user-images.githubusercontent.com/72948843/204659727-963cd991-3895-4c72-a4e4-9c920679791b.png)

The page will load to the overview Heroku app page. Click on 'settings'. Once inside settings, scroll down to the project settings and click 'Reveal Config Vars'. Add the following config vars to the project:
<br>

![image](https://user-images.githubusercontent.com/72948843/204660599-f0e42c6c-de21-4e46-81f5-28f3d082f8c6.png)


Now we have gotten this far, we need to make sure the database URL is ready to receive the new ElephantSQL database. For this we need to install two new packages from pip into the project:

1) Firstly we need to install <strong>dj_database_url</strong> and <strong>psycopg2</strong> for us to connect our external database.
``` pip install dj_database_url==0.5.0 psycopg2 ```
2) Next freeze the requirements in a txt file.
``` pip freeze > requirements.txt ```
3) In settings.py, underneath the import <strong>import os</strong>, import dj_database_url.
``` import os ```
``` import dj_database_url ```
4) Then scroll down to <strong>DATABASES</strong> and update the following code so the original test database that is connected to sqlite3 is temporarily commented out and we can now connect our ElephantSQL database to the project. (as per the picture below)

![image](https://user-images.githubusercontent.com/72948843/204847520-afc8b35b-ee37-4c9d-ac43-8728e802271d.png)

<strong> IMPORTANT! </strong>
DO NOT COMMIT at this point as this will expose your ElephantSQL database link on Github. This is just a temporary measure to prepare our database for migration. It will be removed shortly.

5) In the terminal run <strong>showmigrations</strong> to confirm that it is now connected to the external database.
``` python3 manage.py showmigrations ```

6) If you are, a list of all migrations shall appear but all unchecked.

![image](https://user-images.githubusercontent.com/72948843/204854308-76088d49-f4c1-4054-b2a3-cd168737f4ec.png)

7) Now migrate the database models over to the new database.
 ``` python3 manage.py migrate ```
8) Now the migrations are complte we need to install all fixtures... The products model requires both categories and brands to be set first as they are dependant on this due to the model of products. Follow the order below to successfully load all fixtures that this project requires to get you started.
``` python3 manage.py loaddata categories ```
``` python3 manage.py loaddata brands ```
``` python3 manage.py loaddata products ```
``` python3 manage.py loaddata deliverymethods ```
``` python3 manage.py loaddata camopatterns ```
``` python3 manage.py loaddata weaponplatforms```
``` python3 manage.py loaddata weaponsystems ```
9) Now create a superuser for your new database
``` python3 manage.py createsuperuser ```
10) Now with that complete, we can now unstage step 4, being sure to restore our sqlite3 database as the primary database and removing the ElephantSQL database. Doing this now just prevents us accidentally exposing the database URL for all to see in our repository.

![image](https://user-images.githubusercontent.com/72948843/204858073-459ec562-d225-4c71-b2c7-0cf226f55334.png)

(head over to the database in your elephantSQL file to make sure the migrations were successful)


The next step needed is to avoid posting environmental variables on github and to do this we have to ammend our code in settings. So firstly we need to write an if statement to check if that when our app is running on Heroku where the database URL environment variable will be defined. We connect to Postgres and otherwise, we connect to SQLite.

![image](https://user-images.githubusercontent.com/72948843/204858447-0a7b3dfd-8040-40a6-8c8a-5bc85ec63dd3.png)

Also we need to install <strong>gunicorn</strong>
``` pip install gunicorn ```
Then freeze this into our requirements.txt
``` pip freeze > requirments.txt ```
With that complete, we can create a <strong>Procfile</strong> as the base level in our directory. Inside the file we want Heroku to create a web dyno and gunicorn will host it.

![image](https://user-images.githubusercontent.com/72948843/204861086-f1d89b76-690a-4e9d-b030-c4de41acc455.png)

You can find wsgi_application for your app in the settings.py file

(![image](https://user-images.githubusercontent.com/72948843/204861226-bc6958ba-6725-4279-9a89-54c771045cab.png))

Next login to heroku in the terminal:

![image](https://user-images.githubusercontent.com/72948843/204874022-6bac6a23-8ee7-4ad2-acd4-17552d70dd39.png)(I used the command with -i on the end in gitpod)

Once logged in, run the line below, this ensures that we disable collecting static files.
``` heroku config:set DISABLE_COLLECTSTATIC=1 --app airsoft-workshop ```

![image](https://user-images.githubusercontent.com/72948843/204874624-089d5fa5-9bf8-45f7-99ff-d10f02e06cc6.png)

Next I went to settings.py and added it to our heroku app too the allowed hosts.

![image](https://user-images.githubusercontent.com/72948843/204875408-ebd62a84-775e-4746-a550-e3d1994ca4e5.png)

Now we can add, commmit and push the code to GitHub,
``` git add . ``` 
``` git add . ``` 
``` git add . ``` 
 and after push to heroku too:
``` git push heroku main ```

![image](https://user-images.githubusercontent.com/72948843/204877276-cbf3160e-4ffe-4748-98ee-b4a0622a3934.png)

This appeared because i created the app in the heroku website and not the Heroku CLI, so instead run this command below: 
``` heroku git:remote -a airsoft-workshop ```

![image](https://user-images.githubusercontent.com/72948843/204877848-a28dfe64-d737-4025-be1c-d2ace64d913c.png)

with that now set, run the push to heroku again and it will start to build.

![image](https://user-images.githubusercontent.com/72948843/204880735-bda666ab-c898-41e5-b1b9-23145c52c656.png)

This error occured due to how heroku 22 stack builds and it no longer supports python version 3.8... So to overcome this, in the requirements.txt file on the backports.zoneinfo add the following line of code... 

![image](https://user-images.githubusercontent.com/72948843/204885019-a3657f57-6aa2-498e-9c51-b1177634868f.png)

With that completed, and now deployed, the site works but without the static files. the....

![image](https://user-images.githubusercontent.com/72948843/204884317-8f773f8a-19d4-4175-b302-7fe283c11d3d.png)

Now I moved on to setting up Heroku to deploy automatically when code is committed and pushed to GitHub. to do this, go over to Heroku and within the app, go to deploy and link your GitHub repository to Heroku

![image](https://user-images.githubusercontent.com/72948843/204883925-669ef101-1bd3-4366-aa1b-556ec2f2c425.png).

Click 'Connect'

Now I added a new Secret Key for the project in the Heroku config vars (in the settings page).

![image](https://user-images.githubusercontent.com/72948843/204886753-b3f52d73-9433-4364-830a-8bb34b706025.png)


<!-- ------------------------------------------------------------------------------------------------------------------------------------- -->
<!-- --------------------------------------------------------------------- -->
<!-- CONTINUE TOMORROW from here -->
<!-- --------------------------------------------------------------------- -->



Now go back to VSCode and create a new file called <b><i>env.py</i></b> if it has not already been created. <b>Make sure you add it to your '.gitignore' file</b>. copy the code below. This is nothing new, its just the same config vars from the heroku app and we need them inside our env.py file. make sure to add <b>your</b> config var values inside.

![image](https://user-images.githubusercontent.com/72948843/205462075-424412b9-a0d6-4915-a195-e42f1ce1960a.png)

Inside settings.py, search for the line that says "from pathlib import Path" and then insert the code below:

![image](https://user-images.githubusercontent.com/72948843/182257894-26c2518f-2fbf-401a-b26c-6a845945ecf0.png)

Replace the default random security key that Django provides you with your SECRET_KEY variable that you created in your env.py file.

![image](https://user-images.githubusercontent.com/72948843/182258087-fd940b53-a297-49fa-8445-dcd45aba6892.png)

Set <b>DEBUG = 'DEVELOPMENT' in os.environ</b> This allows you to have Debug set to True when developing locally. However DEBUG will be set to False when deployed to Heroku.

![image](https://user-images.githubusercontent.com/72948843/182258392-dcce5dac-62ea-48fc-a9d0-35e9b5a7d956.png)

Whilst working in development, we want to keep the ElephantSQL for deployment. So, running the code below allows us to have two databases. SQLite for local development and the ElephantSQL database for the deployed application.

![image](https://user-images.githubusercontent.com/72948843/205462193-c7fd414f-4f1e-42ea-a492-f3a3b2deb0f1.png)

Next we need to add a place to store our media and static files for the application... follow the steps in the pdf files below to setup a AMAZON WEB SERVICES bucket to host these files...

<!-- create tidy versions of aws setups as pdfs to put in assets -->
<!-- ------------------------------------------------------------------------------------------------------------------------------------- -->
<!-- --------------------------------------------------------------------- -->
<!-- CONTINUE TOMORROW the pdfs -->
<!-- --------------------------------------------------------------------- -->
<ol>
<li>Setting up a S3 Bucket: <a href="https://github.com/GrantWils23/Portfolio-Project-5--Ecommerce-Applications/blob/main/assets/aws-s3-bucket-services-setup.pdf" taret="_blank">AWS-S3-Bucket setup</a></li>
<li>Setting up the IAM controls: <a href="https://github.com/GrantWils23/Portfolio-Project-5--Ecommerce-Applications/blob/main/assets/aws-iam-setup.pdf" taret="_blank">AWS-IAM setup</a></li>
</ol>

Django to S3...

We now need to install boto3 and django-storages...

``` pip install boto3 ```
``` pip install django-storages ```

Upon successfully downloading the pip packages freeze a copy of the requirements.txt file
``` pip freeze > requirements.txt ```
and then add it to the settings.py file of the app...

![image](https://user-images.githubusercontent.com/72948843/205462317-d8a6959c-df10-489a-8348-54b175eb6936.png)

With that done, we need to write some code to allow us to use the AWS bucket we created... the code is as follows:

![image](https://user-images.githubusercontent.com/72948843/205462422-a7081814-a78d-4bc9-97ab-6eb49272a975.png)

We need to also remove ``` DISABLE_COLLECTSTATIC = 1 ``` inside the heroku settings config vars so when it next deploys it can search for the static and media files.

Next create a new file called ``` custom_storages.py ``` at the base level.

![image](https://user-images.githubusercontent.com/72948843/205463479-28c70918-ee70-489e-9699-fc594f7fa109.png)

Copy the code below into the custom_storages.py file

![image](https://user-images.githubusercontent.com/72948843/205463525-3c54cb10-78db-4f17-936a-0b4b8fc4ce95.png)

Now make sure the variables are added to your heroku apps config vars. add commit and push the files... it will now load and you can see the css static files are working but the media files dont.

The next thing we need to do is add our media files from the media folder into the S3 bucket... This will allow us to then see the images... follow the steps in the pdf below:

- <a href="https://github.com/GrantWils23/Portfolio-Project-5--Ecommerce-Applications/blob/main/assets/caching-media-files.pdf" taret="_blank">>chaching media files</a>

Lastly we need to get stripe working...

add the stripe public and secret keys to the config vars in the heroku apps settings:
![9@ClippedImage](https://user-images.githubusercontent.com/72948843/205464196-13411659-465c-4c9e-ab83-d5dd07208ff5.png)

Lastly we need to create a new endpoint for the webhook to work and add its STRIPE_WH_SECRET to the heorku's config var.

add a new endpoint...
![5@ClippedImage](https://user-images.githubusercontent.com/72948843/205464355-713bf3bc-db51-4638-8f0f-7595460a262b.png)

now add the new signing secret to the heroku settings config vars.
![8@ClippedImage](https://user-images.githubusercontent.com/72948843/205464495-11354d66-aec8-4556-8a5f-415c21efeee5.png)

[Back to Top](<#contents>)

(Side Note: When the app is deployed, Debug has to be set to False! this is for security reasons as it can expose sensative data.)

[Back to Top](<#contents>)

### Setting the email service

The last part that needs setting up is the django emails. Two variables are required... ```['EMAIL_HOST_USER']``` and ```['EMAIL_HOST_PASSWORD']```.

![image](https://user-images.githubusercontent.com/72948843/205464839-789fde98-24b9-4274-bba8-c424eba2e8c5.png)

 I found a really useful tutorial by "Toumi Abderrahmane" on how to set up googlemail sync up to send emails with django in deployment. please click on this link below.

<a href="https://dev.to/abderrahmanemustapha/how-to-send-email-with-django-and-gmail-in-production-the-right-way-24ab" target="_blank">how to send email with django and gmail</a>
<br>

Within the env.py file, at the bottom two lines, you have to insert you email address and password, just look below:

![image](https://user-images.githubusercontent.com/72948843/205464909-c9a511b4-64b6-43a0-bb7b-72c3a3fccb62.png)

Now add these variables to the Heroku's settings config vars.

![image](https://user-images.githubusercontent.com/72948843/205465018-bb55c2d1-8f96-4374-893b-537b26c664ba.png)

Now with this done, you can now send emails in development and deployment.

(Note the code at the bottom of the Development Django Email Settings, this runs in the command line, check here to see if the emails send during development.)

[Back to Top](<#contents>)

<br>

# Cloning and setting up of this project
<hr>



<p>To create a local clone of the project, follow the steps below:</p>

* In the GitHub repository, under the repository name there is a code tab., click on the 'code' tab. and select either HTTPS or CSS link to copy the code. I will use HTTPS:
![image](https://user-images.githubusercontent.com/72948843/182441657-b4116d59-ee58-4a4d-9826-2119bd34d7a8.png)
* In the clone tab, click the HTTPS tab. Within this section, click on the clipboard icon and copy the URL supplied for the repository.

* Once the link has been copied, open an IDE (Command Prompt) of your choosing, navigate to where you wish to store the project and run the following terminal commands:

1. ```"git clone HTTPS or SSH link``` - This will clone the project to your computer
2. ```cd name of project``` - This will cd (change directoy) into your project
3. ```code .``` - This will launch your project in VSCode
<br>
![image](https://user-images.githubusercontent.com/72948843/182444495-9a5f9b21-e7e2-4a99-b055-937a7232470e.png)

Now you need to setup and initialize a virtual environment for the project. follow the steps below to setup a virtual environment if you haven't done so before.

```$ pip install virtualenv```
<br>
(Step.1) Test your installation was successful:

```$ python3 -m virtualenv -- version```
<br>
(Step.2) Then create the virtual environment using virtualenv

```$ python3 -m virtualenv myenv```
<br>

![image](https://user-images.githubusercontent.com/72948843/182444824-9bafb75a-cae4-4cef-b00b-d22d9a619336.png)
<br>
(Step.3) After creating the virtual environment, you need to activate it. <b><i>We need to activate the virtual environment every time you will work on the project!</i></b>. This can be achieved by using the following command:
<br>

* ``` $ source virtualenv_name/bin/activate ``` - [For Mac] 
* ``` $ source virtualenv_name/Scripts/activate ``` - [For Windows]  (as in my example below):

!![image](https://user-images.githubusercontent.com/72948843/182445439-bca1e977-081b-46ea-85c3-312b04543870.png))

<b>Don't forget to addd the env to your .gitignore file</b> if added correctly the file and its content's font shall be shaded a darker grey.

![image](https://user-images.githubusercontent.com/72948843/182445548-45a57c2b-d86a-491e-bd25-3b03f93d0892.png)

Once you are in the virtual environment, the terminal will have it appear in brackets next to the command line as in the image below:

![image](https://user-images.githubusercontent.com/72948843/182445662-f576728c-a54e-48de-92a3-98439108785b.png)

NOTE: To deactivate the virtual environment just type ```deactivate``` into the terminal (like in the image below).

![image](https://user-images.githubusercontent.com/72948843/182445800-b322a679-751f-4ad3-af36-416b91451d23.png)
<br>
<hr>
Now within the virtual environment, we now need to install the project requirements to run the project. in the virtual environment terminal, type in the following command:

```pip3 install -r requirements.txt```

What this will do is download all the app's dependencies stated in the requirements.txt file which will get the project to work.

![image](https://user-images.githubusercontent.com/72948843/182447722-1b86059c-319a-4ef1-9db5-7900de0b4374.png)

With that now complete, We now need to create our env.py file, which tells the app what variables to use. These variables are usually hidden for security reasons as they contain sensative data that we don't want leaked and can be dangerous if shared publicly they can be vulnerable to attacks. So what we must do is first create the env.py file and immediately add it to our .gitignore file.

Any variables you declared in your settings.py file must be added to this file. (Apart from ["DEVELOPMENT"]) to your config vars when you deploy in Heroku.

![image](https://user-images.githubusercontent.com/72948843/182455915-2e6da191-999a-4ffd-8fe4-0494d232e6a0.png)

Now when we run the command ```python3 manage.py runserver``` if the terminal will respond with unapplied migrations which is to be expected as we haven't made any migrations into the database. If this is the case, run the migrations command in the terminal... ```python3 manage.py migrate```.

Once it has finished applying the migrations, you will need to run the command ```python3 manage.py runserver```

![image](https://user-images.githubusercontent.com/72948843/182458479-9d27b5ac-542c-40e4-a11e-2ed937375e73.png)

This will now launch the project locally, successfully and ready for development.

The test files that exist in the project can be run with the simple command ```python3 manage.py test```. 

If you wish to test a particular app you can run the command ```python3 manage.py test "APP_NAME"```

(for example, the specific APP_NAME's from BeBeauty are 'booking' or 'treatment')

This command will only work if you use your local database within the deployment. if for any reason you run this command using the Heroku database, the test will fail. please refer to the <a href="https://github.com/GrantWils23/Portfolio-Project-4--Full-Stack-Toolkit/blob/main/tests/TESTS.md">testing</a> file to see how the tests perform.

This project has installed inside it a python package called [*Coverage*]. This app is useful as it gives you comprehensive reports on how much of your project has been tested. To get a coverage report, run the following command in the terminal: ```coverage report``` and this will output a tabled list of the results from the report. The report gives you an idea of what areas perhaps require more testing and gives you a score on how your tests perform.

<br>

## Credits

<p>Building the website was a very hard process but very rewarding. I would like to mention below some credits to my project:</p>
<ul>
    <li>I used Bootstrap a lot when building this website. I mentioned a link to the website in the above technologies used section.</li>
    <li>Django documentation was used a lot during the build of the website to make sense of how to build the MVT. The documention is very thorough and explains a lot of things clearly. When I had a problem, I could read their docs with a large degree of success</li>
    <li>I also used <a href="https://stackoverflow.com/" target="_blank">Stacker Overflow</a> to help me when I had problems as there was a lot of times people had the same problems as I and I could lean on some of these questions for help.</li>
</ul>
<br>

[Back to Top](<#contents>)

## Acknowledgements

<p>This project is my 4th Portfolio Project, as part of <a href="https://codeinstitute.net/" target="_blank">Code Institute's</a> Full Stack Software Developer (e-Commerce) Diploma.</p> A Big thank you to Precious Ijege (my mentor) for his help and expertise pushing me to right better code. Another thank you to the Slack community as well and Daniel_C_5p_lead (Daniel Callaghan) for his help as he always found the time to reply anytime I had a problem, he always tried to help. Also thank you to the tutors at Code Institute Alex and Oisin who helped me when I lost my way. There experience and help really got my through the tough patches.
<br>
<br>
Grant Wilsmore, 2022
<br>
<br>

[Back to Top](<#contents>)