# Testing

To test my project, I have completed several test procedures and from a wide array of different tests. It is important to test as much of the code as possible. So please scroll down and read the various testing procedures and how I solved some problems with bugs in my code.

## Contents

* [**Testing**](<#testing>)
  * [Code Validation](<#code-validation>)
  * [HTML Validation](<#html-validation>)
  * [CSS Validation](<#css-validation>)
  * [JS Validation](<#js-validation>)
  * [Python Validation](<#python-validation>)
  * [Lighthouse Testing](<#lighthouse-testing>)
  * [Accessibility Testing](<#accessibility-testing>)
  * [Responsive Testing](<#responsive-testing>)
  * [User Story Tests](<#user-story-tests>)
  * [Manual Testing](<#manual-testing>)
  * [Validation Testing](<#validation-testing>)
  * [Automated Testing](<#automated-testing>)
  * [Browser Compatibility](<#browser-compatibility>)
* [**Bugs**](<#bugs>)
  * [Solved Bugs](<#solved-bugs>)
  * [Unsolved Bugs](<#unsolved-bugs>)

## Code Validation

Airsoft Workshop has been validated by using online validation tools W3C HTML Validator, W3C CSS Validator, JSHint JavaScript Validator and the PEP8 Online Validator.
HTML Validation Image... Below are the results of the Validation of the code that I passed through the validator.

## HTML Validation

My HTML Code was directly inputted into the validator from the URI and the results have been recorded below.

### Home HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205744028-443aa29b-4b4c-4c0e-ae43-e616f515bf1e.png)

### Services Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205750877-595645b0-44e9-4dd0-b6ff-363ed6d3469d.png)

### Paint Services Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205752534-96813364-dde5-465d-afd4-7c68b391a00e.png)

### Tech Services Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205752657-0a1655ba-ecd4-437d-b352-4ba78b792b5a.png)

### Thankyou Services Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205771356-96a0734b-8c16-4346-a893-d656b868495a.png)

### Products Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205764232-1e4cd559-a0e2-4b44-9fb4-0111197d6463.png)

### Product Details Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205764445-58b7896b-c7c3-454e-864c-662e5e2597cc.png)

### Basket Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205879868-5ddfe062-45a8-449f-813c-f7003a705dec.png)

### Checkout Page HTML Validation

This was validated using manual input from the local gitpod window, as the direct URI would not work due to the nature of the checkout page.

Due to the way the card payment element is created from the stripe, it creates multiple errors during the test, so I omitted the stripe element from the test procedure.

![image](https://user-images.githubusercontent.com/72948843/205897146-adb258c5-7719-499b-a98e-20c4a985fedf.png)

### Checkout Success Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205898442-bb53a07a-6541-4ef6-b611-d3d215bcafee.png)

### About Us Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205880330-342b275b-2887-471a-914b-25a887817aac.png)

### Contact Us Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205880549-d486d3e7-659b-45d8-98e4-e637fe7dec8c.png)

### FAQs Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205880760-7d950f58-7d36-4a28-94e7-63f3f52fb24c.png)

### Privacy Policy Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205881060-3a903db0-3c9f-45e2-872c-e73512958283.png)

### Sitemap Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205881353-9f83983a-8684-44c2-a475-ec5c2f172afc.png)

### Admin Controls Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205881531-18d3d312-d484-4c17-81bc-092bdcaa4c59.png)

### Add Product Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205876704-cac482bf-50d6-4a26-a5af-28dd239ea801.png)

### Edit Product Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205879273-3e5b09b3-7e2d-43e8-9cfa-7929253396c5.png)

### Add Brand Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205882900-cce92d8d-53b0-42fb-b615-1379fdefb3f5.png)

### Edit Brand Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205883282-95e0c164-839d-494f-a0b7-a1057de084a9.png)

### Add Category Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205881814-2351264f-0265-4e8f-abc5-668f8a5f0cac.png)

### Edit Category Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205882622-becad10a-780b-4e46-b725-856afcab3079.png)

### Add Delivery_Method Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205883725-ca013fde-8189-4d4a-a18c-037c80abbc08.png)

### Edit Delivery_Method Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205884093-29986583-5a40-46da-bbb7-365107b8f958.png)

### Profile Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205886436-5947c7b0-7731-4a5f-a514-a75ef764b956.png)

### Edit Profile Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205886749-5c37fe49-0cd5-45ff-a73d-a6c0411d8e1b.png)

### Change Password Profile Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205886915-e68e196f-902a-45dd-a73e-bc9590bb39cb.png)

### Previous Order History Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205891400-725d994a-75d8-4b18-a7e7-d23eaecb1f1f.png)

### Admin View Orders Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205899235-cd1fc4d8-0055-41ce-b80f-4e593bbde30e.png)

### Admin View Specific Order Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205898765-41ac7a9e-2f89-45cd-aa5a-445a284c51d1.png)

### Admin View Paint Quotes Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205899595-dd058d4a-4b86-43c4-b87c-d2ea7a2c0d0d.png)

### Admin View Specific Paint Quote Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205899942-fafa4c20-0866-45e4-8f75-f6cc0e90455c.png)

### Admin View Tech Quotes Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205900673-fe2ab80a-b56e-4f25-b5fd-97ea7e145ad6.png)

### Admin View Specific Tech Quote Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205900468-bb7b8b9d-b270-42ef-b85a-06fae96b71ea.png)

### Login Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205902738-a0846a31-2bfd-4505-9bf3-769e6f250751.png)

### Register Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205901757-78036e5b-fe98-40a3-a14c-00e8eb77dbf0.png)

### Confirm Email Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205901974-4d49d2ee-64a2-4d2b-8841-e43afaa41324.png)

### Verify Email Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205902126-db08b3d4-1c45-429a-bf95-0fb5aff6d8d1.png)

### Logout Page HTML Validation

![image](https://user-images.githubusercontent.com/72948843/205901066-556e0129-7481-41d5-b62c-598bc54bfe0e.png)

[Back to Top](<#contents>)

## CSS Validation

My CSS Code was directly inputted into the validator and passed with 0 errors.

### Base.CSS Validation

![image](https://user-images.githubusercontent.com/72948843/205928333-0fc14daf-d6db-4b25-b279-cc6431c8c491.png)

### Checkout.CSS Validation

![image](https://user-images.githubusercontent.com/72948843/205923295-5c3ce408-c335-405c-93c6-fcc0a24fb34a.png)

[Back to Top](<#contents>)

### JS Validation

The JS Code in my program appears across multiple files in the app, I have multiple script tags located at the bottom of many HTML templates in this project. I also had two dedicated javascript files, one located in a static folder in the checkout app, and the other in the profiles app. The checkout app contains the code for Stripe to work which is the only dedicated file that uses a lot of JS. The profiles javascript contains the code to use the countries field which is referenced across two pages in the website. To run checks on my code, I passed the code through JSHint which is a code validator for JS. In the product app, one of the javascript code was written in a HTML page. The results for the validations were also recorded.

Below I have recorded the results of my Javascript validations:

* Checkout / stripe_elements.js JavaScript

![image](https://user![image](https://user-images.githubusercontent.com/72948843/205941873-00980434-a11b-4bb1-bcf6-146dee65b090.png)

* Profile / countryfield.js JavaScript

![image](https://user-images.githubusercontent.com/72948843/205944883-4c534e6a-19ad-4995-947d-b5f30f357604.png)

* Basket / basket.html JavaScript

![image](https://user-images.githubusercontent.com/72948843/205946374-40e6a2bb-247e-40be-8554-995212ce953c.png)

* Product / quantity_input_script.html

![image](https://user-images.githubusercontent.com/72948843/205947913-f74f62c3-ee20-4d77-bfff-72eece8be004.png)

[Back to Top](<#contents>)

## Python Validation

My Python Code was directly checked for errors inside the terminal using the command ``` python3 -m flake8 ```.
I am happy with flake8 report as the vast majority of these errors reported are lines to long on auto generated files, and changing these could harm the files for migrations, so i opted to leave these alone. The remaining files that have been flagged with errors are import errors not being tracked, where a import cannot be found unless tests are running. 

### PEP* Validator using Flake8

![image](https://user-images.githubusercontent.com/72948843/206061147-4a059c2d-1026-48d3-91d5-fdff6bcf07c6.png)

![image](https://user-images.githubusercontent.com/72948843/206062334-d66b5f33-3253-48b6-b74b-95d189049d1a.png)

![image](https://user-images.githubusercontent.com/72948843/206062513-dea0c561-03c7-44cb-b43c-3b9d193c5f14.png)

[Back to Top](<#contents>)

## Lighthouse Testing

To check the production levels against its performance, I used the Lighthouse testing facilities in the chrome development tools. Below are the results on how the pages performed in both Desktop and a responsive view.

* Home page - PC view

![image](https://user-images.githubusercontent.com/72948843/206146892-ab82eca0-11c5-4d78-876b-58b1c2380705.png)

* Home page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206150009-129a7a9c-f9ad-4c1e-93b3-7179058393a9.png)

<!--  -->

* Services page - PC view

![image](https://user-images.githubusercontent.com/72948843/206159904-a0400ac5-71a6-44c3-b2b5-4dd3d3bdb86d.png)

* Services page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206159677-2a85a894-085d-4db5-8161-c3611cfcdd5f.png)

<!--  -->

* Paint Services Quote page - PC view

![image](https://user-images.githubusercontent.com/72948843/206161123-1facaf75-2790-4f88-8d71-9973c2266317.png)

* Paint Services Quote page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206160945-d1154fe4-0332-4245-8b74-507e0f435b1c.png)

<!--  -->

* Tech Services Quote page - PC view

![image](https://user-images.githubusercontent.com/72948843/206161630-89c6bd7b-ae74-4884-b513-075d053d7c52.png)

* Tech Services Quote page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206161465-5acdc978-61d9-428f-be53-816be37c4aea.png)

<!--  -->

* Thank You Services Note page - PC view

![image](https://user-images.githubusercontent.com/72948843/206162258-726070cc-2bc3-4469-9e93-dc808fb9e7e6.png)

* Thank You Services Note page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206161465-5acdc978-61d9-428f-be53-816be37c4aea.png)

<!--  -->

* Store page - PC view

![image](https://user-images.githubusercontent.com/72948843/206163587-e6055f9a-59e8-41f1-babd-a20da6ef3048.png)

* Store page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206162937-7d403411-af44-4e5f-9add-097ebb547e41.png)

<!--  -->

* Product Detail page - PC view

![image](https://user-images.githubusercontent.com/72948843/206162258-726070cc-2bc3-4469-9e93-dc808fb9e7e6.png)

* Product Detail page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206161465-5acdc978-61d9-428f-be53-816be37c4aea.png)

<!--  -->

* Basket page - PC view

![image](https://user-images.githubusercontent.com/72948843/206180539-65d70399-0208-4345-8deb-8f10c9ce8bbd.png)

* Basket page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206181288-ead2fb29-60fd-4d77-9959-9af58b93aa23.png)

<!--  -->

* Checkout page - PC view

![image](https://user-images.githubusercontent.com/72948843/206181915-16cf01d4-72c5-4c95-acba-b35328c52bea.png)

* Checkout page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206181690-c8b44c7f-5c9a-4507-93e5-439f49081f23.png)

<!--  -->

* Checkout success page - PC view

![image](https://user-images.githubusercontent.com/72948843/206182230-6f9da288-2f82-4116-b566-b20aef61a2b0.png)

* Checkout success page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206182577-edbbd8a4-21c0-485b-b735-4ab618dbc293.png)

<!--  -->

* Profiles page - PC view

![image](https://user-images.githubusercontent.com/72948843/206183006-f44c4fcc-1627-4a40-85cc-931b1673db79.png)

* Profiles page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206182815-70690084-7fbd-4e88-8240-6d90ee79dc05.png)

<!--   -->

* Update profile page - PC view

![image](https://user-images.githubusercontent.com/72948843/206239673-c6db2d3f-08d2-4b7b-bcb5-b4b4e9bb6588.png)

* Update profiles page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206240876-5e4453f8-9512-439a-b76a-00be9bd284ba.png)

<!--  -->

* Update password page - PC view

![image](https://user-images.githubusercontent.com/72948843/206242254-78f6080c-e55f-43f1-b53f-68d7908d5cae.png)

* Update password page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206242765-5a742426-4c67-4213-bd45-d967676e554e.png)

<!--  -->

* Contact Us page - PC view

![image](https://user-images.githubusercontent.com/72948843/206243384-5fd3a4b0-0d25-466c-a0fa-07a861685e24.png)

* Contact Us page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206243034-66e89de7-3131-491d-97a0-28a66228d34b.png)

<!--  -->

* About Us page - PC view

![image](https://user-images.githubusercontent.com/72948843/206243672-a0bf4776-5e1c-4826-9d54-2b20e5bd702a.png)

* About Us page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206244047-7136f54c-d09c-4d13-90b5-da26a73a1c05.png)

<!--  -->

* FAQs page - PC view

![image](https://user-images.githubusercontent.com/72948843/206244606-18ad5109-bb62-4888-9115-7c18fcaacea5.png)

* FAQs page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206244356-113347fe-80fd-449f-858d-0aef0d854f6e.png)

<!--  -->

* Privacy Policy page - PC view

![image](https://user-images.githubusercontent.com/72948843/206246237-a1cd61bc-f2ae-42bc-9161-f9a2c88386da.png)

* Privacy Policy page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206246522-2e252c82-5376-42dd-b559-f4856e337a62.png)

<!--  -->

* Sitemap page - PC view

![image](https://user-images.githubusercontent.com/72948843/206246890-74b430e6-a999-4423-981a-a00946efa41b.png)

* Sitemap page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206247133-dcdb500f-b669-473e-b3c1-eb55685a59a5.png)

<!--  -->

* Store Management page - PC view

![image](https://user-images.githubusercontent.com/72948843/206247826-d660b17d-3539-438b-883b-957eba3fd00d.png)

* Store Management page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206247481-2f3116b3-808c-4e03-8296-5e1df4276a1d.png)

<!--  -->

* Add Product page - PC view

![image](https://user-images.githubusercontent.com/72948843/206248456-44891107-f766-4cac-a339-1eecb8912341.png)

* Add Porduct page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206248751-25f20003-b1ed-4e93-9ecf-d719549b01ac.png)

<!--  -->

* Edit Product page - PC view

![image](https://user-images.githubusercontent.com/72948843/206253501-d8001ace-4d1c-4e76-9441-b2d3cce10091.png)

* Edit Porduct page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206254309-202b1ed2-bf7b-4e12-bb47-816f9e308795.png)

<!--////////////////////////////////////////////////////////////////////////  -->

* Add Brand page - PC view

![image](https://user-images.githubusercontent.com/72948843/206258616-6335f035-3510-44ba-840c-331ae59885a8.png)

* Add Brand page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206257509-e4ecb1fe-b6aa-40c9-bd68-9b4b43bfb863.png)

<!--  -->

* Edit Brand page - PC view

![image](https://user-images.githubusercontent.com/72948843/206259291-0620ef6e-16bf-4701-b016-bc482bc96d16.png)

* Edit Brand page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206259716-cede9c29-5986-4c73-b308-4d7bec80f223.png)

<!--  -->

* Add Category page - PC view

![image](https://user-images.githubusercontent.com/72948843/206260003-8904fa89-49e4-44c4-8e55-bfb179a06a7e.png)

* Add Category page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206260167-15d09bfd-8398-4322-b3db-152594177218.png)

<!--  -->

* Edit Category page - PC view

![image](https://user-images.githubusercontent.com/72948843/206260446-891bafcb-e05f-420a-94d3-f0942c88752c.png)

* Edit Category page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206260641-676d6f8b-c16c-4c75-9510-80a4261dbf81.png)

<!--  -->

* Add Delivery Method page - PC view

![image](https://user-images.githubusercontent.com/72948843/206260838-0e9d5bf0-2dbe-457f-8ab2-220fe61479b0.png)

* Add Delivery Method page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206261000-ccc9dd4d-7bae-4ae0-8b27-7ce4a24c6f17.png)

<!-- -->

* Edit Delivery Method page - PC view

![image](https://user-images.githubusercontent.com/72948843/206261366-050fb818-b0e6-490d-ad5f-c67cb023cf49.png)

* Edit Delivery Method page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206261513-1b163e78-d2f3-4e61-a692-d4695c47477b.png)

<!-- -->

* Admin View Orders page - PC view

![image](https://user-images.githubusercontent.com/72948843/206262044-8cb10a54-3ded-4d98-8e69-22f53852ff0c.png)

* Admin View Orders page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206262193-b43ff32b-9efe-4618-9262-789efc4d9def.png)

<!-- -->

* Admin View Specific Order page - PC view

![image](https://user-images.githubusercontent.com/72948843/206262387-3ca6d04c-98e0-4e23-a704-c0a0fcdb0eca.png)

* Admin View Specific Order - mobile view

![image](https://user-images.githubusercontent.com/72948843/206262582-ae20b40f-7e31-4931-8bb4-588ca6926ebf.png)

<!-- -->

* Admin View Paint Requests page - PC view

![image](https://user-images.githubusercontent.com/72948843/206263404-230a7273-a9d3-49e6-8f16-2ef9a2370afa.png)

* Admin View Paint Requests page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206264151-270d4ae2-fcec-49a7-a2ea-4445e73a14d6.png)

<!-- -->

* Admin View Specific Paint Request page - PC view

![image](https://user-images.githubusercontent.com/72948843/206266968-9b2c8195-d269-4570-b4a5-ce228159c9fc.png)

* Admin View Specific Paint Request page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206267125-79dbf220-90e7-4a93-a8ea-85a43b39230f.png)

<!-- -->

* Admin View Tech Requests page - PC view

![image](https://user-images.githubusercontent.com/72948843/206268169-ddfb54b7-7d3b-4b15-9d89-aef1f5668538.png)

* Admin View Tech Requests page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206268780-8aa178d1-e6aa-4d2d-b980-eece1bebae3c.png)

<!-- -->

* Admin View Specific Tech Request page - PC view

![image](https://user-images.githubusercontent.com/72948843/206269173-9f86780b-02f3-43aa-92fa-3853de550f8f.png)

* Admin View Specific Tech Request page - mobile view

![image](https://user-images.githubusercontent.com/72948843/206269364-e06fe28f-1984-4fac-b430-70c27c94a450.png)

<!-- -->

The results were very positive and successful. I used the feedback from initial lighthouse checks to improve teh quality of these results. Along the way I had found SEO failuers in some of my tags  and buttons not labelled. I addressed these issues and this immediately improved the results and got me into the green.

I also found some accessibility issues, with my text-to-background contrast ratio not being sufficiently high enough to satisfy a high score. So I addressed this issue by increasing the brightness of the font and no longer using the bootstrap secondary-text colour.

There was one concern with the performance running at a lower performance accross all mobile views. the performance checks of the lighthouse did however give me some feedback on the reason for this...

![image](https://user-images.githubusercontent.com/72948843/206273403-457bb0d4-7741-4597-96bb-4855ca468abe.png)

I did try incognito mode to see if it would improve the performance of the mobile view and unfortunately, it did not. With my chrome extensions setup perfectly how I require it, I and not having access to another chrome pc, I decided to just check the performance manually. The deployed app performs well in real-life tests and is documented in a section further down in this file.

I am really happy with these results as they demonstrate that the website passed a lot of the criteria of a high-standard app.

[Back to Top](<#contents>)
<br>

<!-- continue from here -->

## Accessibility Testing

I used a website called <a href="https://color.a11y.com/" target="_blank">A11y</a> which is an accessibility validator to check the colour of the font against the background. I ran a few pages through the validation checker and the results are recorded below.

* Products Page
![image](https://user-images.githubusercontent.com/72948843/206296404-83a2d2e0-214c-48fb-b2d7-1116474f6ff8.png)
![image](https://user-images.githubusercontent.com/72948843/206297690-2ccd0da5-b4cf-40bc-956f-58ffbea80633.png)

* User Profile Page
![image](https://user-images.githubusercontent.com/72948843/206298533-87c1376e-c213-417d-b1d3-e8873e70ad18.png)
![image](https://user-images.githubusercontent.com/72948843/206298838-ee37a652-3e37-4671-98b1-3a9bd41e6f83.png)

 The website passes, with some noted fails. The logo font is an important part of the brand image, but fails its contrast ration on smaller text. Due to the size of were these items are, they don't pose much of an issue as the font never reduces to an unreadable that the aspect ratio is going to be a problem. With these results, I am happy moving forward in my testing knowing that the website accessibility rating is high.

[Back to Top](<#contents>)

## Responsive Testing

To do my Responsive checks of the page, I done manual checks to ensure the page responsed well at different aspect ratios. during this test i found that my footer was moving up the page and generating deadspace beneath it which was not pretty and gave a poor user experience... I made some css changes to fix this issue so now the footer alwatys sits on the bottom of the page. The results following the corrections are recorded in a spreadsheet below:

![image](https://user-images.githubusercontent.com/72948843/206443633-59f0466b-294e-4245-8ece-483819aed3ac.png)

[Back to Top](<#contents>)

## User Story Tests

### EPIC 1 (VIEWING AND NAVIGATION)

#### User Story 1

As a shopper, i can view a list of products i wish to purchase.
   This user can browse the products in a list of products in the store and click on a selected item and add it to the basket.

#### User Story 2

As a shopper, I am able to view and individual product, so that I can identify the price, descritpion, product rating and product image.
   This is achieved when the user clicks on the image in the card from the products view, it takes them into the product detail page. Here the user can see the description along with the price rating and image.

#### User Story 3

As a shopper, I can quickly identify categories and brands, so that I can find products by a general category or brand.
   under each product there is a little tags stating the brand and category of the item. When you click on the tag, it acts a tag to search products by the tag selected.

#### User Story 4

As a shopper, I can Easily View the total of what I am about to purchase, so that I can avoid spending too much money.
   

[Back to Top](<#contents>)

## Manual Testing

following the above User Story Tests, those tests coincide with the manual testing procedures of the website. A lot of the features above where check through manual testing to ensure a great user experience. Below is a list of the some of the features manually tested.

![image](https://user-images.githubusercontent.com/72948843/206440175-9b024cc7-471f-4e5d-885e-010d64d24224.png)
![image](https://user-images.githubusercontent.com/72948843/206440548-5f02a36e-42ed-4e87-a5a3-83064b249d32.png)
![image](https://user-images.githubusercontent.com/72948843/206440632-3cb5bfae-2164-4991-9020-76f1d4ee9ba7.png)
![image](https://user-images.githubusercontent.com/72948843/206441539-7795fd13-3236-4dd2-92f1-876f0bb08697.png)
![image](https://user-images.githubusercontent.com/72948843/206441655-cff2be78-3858-4793-a384-14b9a3298f32.png)
![image](https://user-images.githubusercontent.com/72948843/206441751-621e9e6a-97d2-4860-9262-2a68bad505f0.png)
![image](https://user-images.githubusercontent.com/72948843/206441891-1200249b-45da-4040-b34f-648639374f85.png)
![image](https://user-images.githubusercontent.com/72948843/206441963-a91fb7b2-65af-4f89-acee-2a9ddfa813b8.png)
![image](https://user-images.githubusercontent.com/72948843/206442056-54c925b3-e4f6-4ee8-b27d-7c65bd344e86.png)

[Back to Top](<#contents>)

## Validation Testing

### Validation checks

Validation of the form is implemented by checking before the document is submitted is valid to submit. This is achieved by multiple methods:

* To validate the phone number being entered into the form, django-phonenumber-field was used. It checks the input to see if it is a valid phone number and returns an error message if it is not valid upon submission. This inbuild validation was used on the profile, tech and paint services models but not the Order Model.
* To validate the country field, django-countries were used. It checks whether the data entered into the field is entered correctly.

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

## Automated Testing

To check the code, I ran <a href="https://pypi.org/project/coverage/" target="_blank">Coverage</a> (A Third party package) to check how well my Automated tests performed

* I created and ran 9 tests, with coverage report of 43% statments tested to 57% missed.
* To run these tests, you need to run the command <i>"python3 manage.py test"</i> in the terminal.

![image](https://user-images.githubusercontent.com/72948843/206062848-5cdda1b1-3b4d-4984-bf8a-830d82c549d7.png)
![image](https://user-images.githubusercontent.com/72948843/206063262-7222dcb4-9d9b-4e4b-8d06-2c3eea1de224.png)

Ideally with more time I would like to imporve this figure so that it is at least 70% but with a lack of time, and the majority of testing done being manual, it is something that I definitely would look to improve, going forward.

[Back to Top](<#contents>)

## Bugs

### Solved Bugs

I had found a bug whereby if a user placed an order as a unregistered user, the code in my webhookhandler.py would not be able to find the order that was generated at the checkout view. This in turn created a double booking in the database, one for the frist correct order that had the right value charged by stripe, the second order will be the incorrect order with the wrong order information being inserted into the order with incorrect information regarding the grand total paid and shipping method cost changing and then the customer getting the wrong information was sent to them on the email.

After lots of time spent trying to find the fault for this, I had found that it was the django-phonenumber-field used in the model that was causing the problem. during the order process, it would not validate correctly, the order would be created before the forms self-validation would take place and it would cause the site to crash. Therefore decided to remove this from the order model and just keep it in the user profile form. That way, if the user sets up their profile first the form will validate the number here and it will be correct when the saved data gets used at checkout. if the user updates the profile, if for ever reason the telephone number is wrong, the form will prompt the user to make sure it is a valid telephone number.

[Back to Top](<#contents>)

### Unsolved Bugs

There are no unfixed bugs found on the project.

[Back to Top](<#contents>)

### Browser Compatibility

The Website was manually tested in different browsers to check the responsive nature of the website and no errors were found during these tests.

* Google Chrome
* Microsoft Edge
* Safari
* Samsung Internet

[Back to Top](<#contents>)
