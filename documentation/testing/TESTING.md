# Testing

## Overview

This document records the testing carried out for Cities Under Watch across manual functional testing, user story testing, validation, Lighthouse auditing, and bug tracking. Testing was completed on both local and deployed versions of the site to confirm that core user journeys, admin workflows, responsiveness, and supporting content behaved as expected.

## Manual Functional Testing

### Navigation and Layout

| Test ID | Feature | Test | Expected Result | Actual Result | Pass/Fail | Notes |
|---------|---------|------|-----------------|---------------|-----------|-------|
| NAV-01 | Logo Navigation | Click the site logo from all major pages | User returns to homepage from each page | Site logo returned the user to the homepage from all major pages tested | PASS |  |
| NAV-02 | Main Navigation | Click each main navigation link in the desktop header | Each link opens the correct page | Each desktop header navigation link opened the correct page | PASS |  |
| NAV-03 | Mobile Navigation | Open the mobile menu and click each navigation link | Mobile menu opens correctly without layout issues | Mobile menu opened correctly and each navigation link routed to the correct page without layout issues | PASS |  |
| NAV-04 | Mobile Menu Toggle | Open and close the mobile menu using the toggle | Menu opens and closes correctly without layout issues | Mobile menu toggle opened and closed the menu correctly without layout issues | PASS |  |
| NAV-05 | Mobile Menu Keyboard Close | Open the mobile menu and press Escape | Mobile menu closes correctly | Mobile menu closed correctly when Escape was pressed | PASS |  |
| NAV-06 | Header Account Links | Click account-related header links in logged-out and logged-in states | Correct links display for each user state and route correctly | Header account links displayed correctly for each authentication state and routed to the correct pages | PASS |  |
| NAV-07 | Header Bag Link | Click the bag icon/link from multiple pages | User is taken to the bag page | Bag icon/link routed correctly to the bag page from the pages tested | PASS |  |
| NAV-08 | Footer Explore Links | Click all links in the Explore footer column | Each footer link opens the correct page | All footer Explore links opened the correct pages | PASS |  |
| NAV-09 | Footer Account Links | Click all links in the Account footer column in logged-out and logged-in states | Each link opens the correct page and behaves correctly for authentication state | Footer Account links behaved correctly for logged-out and logged-in states and opened the correct pages | PASS |  |
| NAV-10 | Footer Legal Links | Click all legal links in the footer | Each legal page opens correctly | All legal footer links opened the correct pages | PASS |  |
| NAV-11 | Footer Social Links | Click each social media icon/link | Each link behaves as intended and opens the correct destination or placeholder behaviour | Footer social media links opened the correct external destinations as intended | PASS | |
| NAV-12 | Homepage Primary CTAs | Click primary CTA buttons on the homepage, such as Shop and Browse | Each CTA opens the correct destination page | Homepage primary CTAs opened the correct destination pages | PASS |  |
| NAV-13 | Section CTA Buttons | Click section-level CTA buttons across major pages | Each CTA opens the correct target page or anchor location | Section-level CTA buttons routed correctly to their intended pages or anchor locations | PASS |  |
| NAV-14 | Breadcrumb Navigation | Click breadcrumb links on product and collection detail pages | Breadcrumb links return the user to the correct parent pages | Breadcrumb links returned the user to the correct | PASS | |
| NAV-15 | In-Page Anchor Links | Click anchor links such as Browse prints, View order summary, or newsletter links | User is moved to the correct section on the page | In-page anchor links moved the user to the correct section on the page | PASS | |
| NAV-16 | Page Load Layout | Open each major page on desktop | Layout loads without broken spacing, overlap, or missing sections | Major pages loaded correctly on desktop without broken spacing, overlap, or missing sections | PASS | |
| NAV-17 | Mobile Layout | Open each major page on mobile viewport | Layout remains readable, usable, and visually consistent on small screens | Major pages remained readable, usable, and visually consistent on mobile | PASS | |
| NAV-18 | Tablet Layout | Open each major page on tablet viewport | Layout remains stable and usable on table screen sizes | Major pages remained stable and usable on tablet screen sizes | PASS | |
| NAV-19 | Image Loading | Review major pages containing static and media images | Images load correctly without distortion, missing files, or broken paths | Images loaded correctly on the pages tested without distortion, missing files, or broken paths | PASS | |
| NAV-20 | Button Consistency | Review buttons across major pages | Buttons are styled consistently and remain readable and clickable | Buttons were styled consistently and remained readable and clickable across the pages tested | PASS | |
| NAV-21 | Focus States | Navigate key links and button using keyboard tabbing | Visible focus states appear clearly on interactive elements  | Visible focus states appeared clearly on interactive elements during keyboard navigation | PASS | |
| NAV-22 | Error Page Layout | Open custom error pages such as 404 and 500 where possible | Error pages display correctly and match site layout and branding | Custom error pages displayed correctly and matched the site layout and branding where tested | PASS | |

### Static Pages

| Test ID | Feature | Test | Expected Result | Actual Result | Pass/Fail | Notes |
|---------|---------|------|-----------------|---------------|-----------|-------|
| STA-01 | Homepage | open the homepage on the deployed site | Homepage loads correctly with hero content, featured sections, images, and working CTAs | The homepage loaded correctly on the deployed site with hero content, featured sections, images, and working CTAs | PASS | |
| STA-02 | About Page | Open the About page | About page loads correctly with all text, images, and CTAs visible | The About page loaded correctly with all text, images, and CTAs visible | PASS | |
| STA-03 | Contact Page | Open the Contact page | Contact page loads correctly with contact form, support content, and working layout | The Contact page loaded correctly with contact form, support content, and working layout | PASS | |
| STA-04 | FAQ Page | Open the FAQ page | FAQ page loads correctly will all questions, answers, and suppport links visible | The FAQ page loaded correctly with all questions, answers, and support links visible | PASS | |
| STA-05 | Privacy Policy | Open the Privacy Policy page | Privacy Policy page loads correctly with full content and correct formatting | The Privacy Policy page loaded correctly with full content and correct formatting | PASS | |
| STA-06 | Terms and Conditions | Open the Terms and Conditions page | Terms and Conditions page loads correctly with full content and correct formatting | The Terms and Conditions page loaded correctly with full content and correct formatting | PASS | |
| STA-07 | Refund Policy | Open the Refund Policy page | Refund policy page loads correctly with full content and correct formatting | The Refund Policy page loaded correctly with full content and correct formatting | PASS | |
| STA-08 | Delivery Policy | Open the Delivery Policy page | Delivery Policy page loads correctly with fill content and correct formatting | The Delivery Policy page loaded correctly with full content and correct formatting | PASS | |
| STA-09 | Static Images | Review all static content pages for image loading | All static images load correctly without broken link paths or distortion | Static images loaded correctly across the static content pages tested without broken paths or distortion | PASS | |
| STA-10 | Placeholder Content Check | Review all static pages for leftover placeholder text or placeholder blocks | No placeholder copy, placeholder images, or unfinished sections remain | No placeholder copy, placeholder images, or unfinished sections were found on the static pages tested | PASS | |
| STA-11 | Static Page CTA Links | Click all CTA buttons and support links on static pages | Each CTA or internal link routes to the correct page or section | Static page CTA buttons and support links routed correctly to the intended pages or sections | PASS | |
| STA-12 | Contact Form Visibility | Review the contact form fields and labels on the Contact page | All required fields, labels, and button are visible and readable | All required contact form fields, labels, and button were visible and readable | PASS | |
| STA-13 | FAQ Accordion Behaviour | open and close FAQ accordion items | FAQ accordion items expand and collapse correctly without layout issues | FAQ accordion items expanded and collapsed correctly without layout issues | PASS | |
| STA-14 | Typography Consistency | Review headings, paragraphs, and spacing across static pages | Typography hierarchy and spacing remain consistent across pages | Typography hierarchy and spacing remained consistent across the static pages tested | PASS | |
| STA-15 | Desktop Static Layout | Open all static pages on desktop | Layout is stable, readable, and visually consistent on desktop | Static page layouts were stable, readable, and visually consistent on desktop | PASS | |
| STA-16 | Mobile Static Layout | Open all static pages on mobile | Layout is stable, readable, and visually consistent on mobile | Static page layouts were stable, readable, and visually consistent on mobile | PASS | |
| STA-17 | Tablet Static Layout | Open all static pages on table | Layout is stable, readable, and visually consistent on tablet | Static page layouts were stable, readable, and visually consistent on tablet | PASS | |
| STA-18 | Error-Free Page Load | Open each static page and monitor visible template or rendering issues | Pages load without template errors, broken components, or missing sections | Static pages loaded without template errors, broken components, or missing sections | PASS | |

### Catalogue and Collections

| Test ID | Feature | Test | Expected Result | Actual Result | Pass/Fail | Notes |
|---------|---------|------|-----------------|---------------|-----------|-------|
| CAT-01 | Catalogue Page | Open the Shop / Catalogue page | Catalogue page loads correctly with page header, intro section, product grid, and collection showcase | The catalogue page loaded correctly with the page header, intro section, product grid, and collection showcase visible | PASS | |
| CAT-02 | Active Products Display | Review the catalogue product grid | All active products are displayed in the catalogue | All active products were displayed correctly in the catalogue grid | PASS | |
| CAT-03 | Product Card Content | Review multiple product cards | Each card shows the correct image, title, and price | Each product card displayed the correct image, title, and price | PASS | |
| CAT-04 | Product Card Links | Click multiple product cards from the catalogue | Each card links to the correct product detail page | Each product card linked to the correct product detail page | PASS | |
| CAT-05 | Catalogue Search | Search for a known product title or keyword | Matching products are returned correctly | Catalogue search returned the expected matching products correctly | PASS | |
| CAT-06 | Catalogue Search No Results | Search for a term with no matching products | No results state displays appropiately without errors | The catalogue displayed a clear no-results state without errors when no products matched the search term | PASS | |
| CAT-07 | Collection Filter Toggle | Open and close the filter panel on the catalogue page | Filter panel opens and closes correctly | The filter panel opened and closed correctly on the catalogue page | PASS | |
| CAT-08 | Collection Filter Selection | Select a collection filter on the catalogue page | Only products from the selected collection are shown | Selecting a collection filter correctly showed only products from the selected collection, but the page refreshed and jumped back to the prints section, creating an unpleasant user experience | PASS | Filtering works correctly, but the page refresh and forced scroll back to the prints section creates an unpleasant UX |
| CAT-09 | Clear Filters | Click the Clear link after using search and/or filters | Search term and filters are cleared and full catalogue view returns | The Clear link reset the search term and filters correctly and returned the full catalogue view, but the page refreshed and jumped back to the prints section, creating an unpleasant user experience | PASS | Clear filters works correctly, but the page refresh and forced scroll back to the prints section creates an unpleasant UX |
| CAT-10 | Load More Pagination | Click the Load more button when more products are available | Additional products are revealed correctly without losing current filters/search state | The Load more button revealed additional products correctly without losing the current filters or search state, but the page refreshed and jumped back to the prints section, creating an unpleasant user experience | PASS | Load more works correctly, but the page refresh and forced scroll back to the prints section creates an unpleasant UX |
| CAT-11 | Collection List Page | Open the Collection page | Collection list page loads correctly with all available collections | The collection list page loaded correctly and displayed the available collections | PASS | |
| CAT-12 | Collection Card Content | Review collection cards on the Collections page | Each card shows image, collection name, city, and print count correctly | Each collection card displayed the correct image, collection name, city, and print count, and the card layout aligned correctly across breakpoints | PASS | Collection card alignment and CTA layout updated |
| CAT-13 | Collection Card Links | Click multiple collection cards/buttons | Each collection opens the correct collection detail page | Each collection card and button opened the correct collection detail page | PASS | |
| CAT-14 | Collection Detail Page | Open a collection detail page | Collection detail page loads correctly with collection info and related products | The collection detail page loaded with the collection information, but the story section showed a placeholder because there is no dedicated image field in the model for the collection story media | FAIL | Add a dedicated image field for the collection story/support media section so the placeholder can be replaced with real content |
| CAT-15 | Collection Product Display | Review products shown on a collection detail page | Only products belonging to that collection are shown | Only products belonging to the selected collection were displayed on the collection detail page | PASS | |
| CAT-16 | Collection Detail Navigation | Use collection detail page links and CTAs | links route correctly oy related pages such as products or other collections | Collection detail page links and CTAs routed correctly to the expected pages and sections | PASS | |
| CAT-17 | Featured Collection Display | Review the featured collection section on the catalogue page | Featured collection displays correctly with correct content and link | The featured collection section displayed correctly with the expected content and working link | PASS | |
| CAT-18 | Coming Soon Collections | Review the coming soon collection cards on the catalogue page | Coming soon collections display correctly with planned print counts and notify link | Coming soon collection cards displayed correctly with planned print counts and the notify link | PASS | |
| CAT-19 | Related Collection Discovery | Review other collections / additional collection sections | Related or additional collections display correctly and link as expected | Related and additional collections displayed correctly and linked as expected | PASS | |
| CAT-20 | Empty Catalogue State | Test catalogue behaviour if no products match filters/search | Page remains stable and displays a clear empty state message | The catalogue remained stable and displayed a clear empty state message when no products matched the search or filter | PASS | |
| CAT-21 | Catalogue Images | Review catalogue and collection pages for image loading | All product and collection images load correctly without distortion or broken paths | Most product and collection images loaded correctly, but one image was missing from the collection detail page | FAIL | A collection detail page asset is missing and needs to be added or correctly linked |
| CAT-22 | Catalogue Desktop Layout | Open catalogue and collection pages on desktop viewport | Layout is stable, reusable, and visually consitent on desktop | Catalogue and collection pages remained stable and visually consistent on desktop | PASS | |
| CAT-23 | Catalogue Mobile Layout | Open catalogue and collection pages on mobile viewport | Layout is stable, reusable, and visually consitent on mobile | Catalogue and collection pages remained usable on mobile, but the search and filter section required realignment | FAIL | Search and filter controls on mobile need spacing and alignment adjustments |
| CAT-24 | Catalogue Tablet Layout | Open catalogue and collection pages on tablet viewport | Layout is stable, reusable, and visually consitent on tablet | Catalogue and collection pages remained stable and visually consistent on tablet | PASS | |
| CAT-25 | Catalogue Admin Links | View catalogue and product cards as superuser | Edit and delete admin links display only for superuser where expected | Admin edit and delete links displayed correctly for the superuser where expected | PASS | |
| CAT-26 | Catalogue Admin Link Restriction | View catalogue and product cards as a normal user or logged-out user | Admin edit/delete links are hidden from unauthorised users | Admin edit and delete links were hidden from normal users and logged-out users | PASS | |
| CAT-27 | Catalogue Add Product Link | View the catalogue page as a superuser and click the Add product button | Add product button is visible to superuser and opens the add product page correctly | The Add product button was visible to the superuser and opened the add product page correctly | PASS | |
| CAT-28 | Catalogue Add Product Restriction | View the catalogue page as a logged-out user and as a normal authenticated user | Add product button is hidden from unauthorised users | The Add product button was hidden from logged-out users and normal authenticated users | PASS | |
| CAT-29 | Collection Add Product Link | View a collection detail page as a superuser and click the Add product button | Add product button is visible to superuser and opens the add product page correctly | The Add product button was visible to the superuser on the collection detail page and opened the add product page correctly | PASS | |
| CAT-30 | Collection Add Product Restriction | View a collection detail page as a logged-out user and as a normal authenticated user | Add product button is hidden from unauthorised users | The Add product button was hidden from logged-out users and normal authenticated users on the collection detail page | PASS | |

### Product Detail and Bag

| Test ID | Feature | Test | Expected Result | Actual Result | Pass/Fail | Notes |
|---------|---------|------|-----------------|---------------|-----------|-------|
| PDB-01 | Product Detail Page | Open multiple product detail pages from the catalogue and collection pages | Each product detail page loads correctly with title, price, description, gallery, and purchase options | Multiple product detail pages loaded correctly with title, price, description, gallery, and purchase options visible | PASS | |
| PDB-02 | Product Gallery | Click each thumbnail image on a product detail page | Main product image updates correctly to match the selected thumbnail | The main product image updated correctly when each thumbnail was selected | PASS | |
| PDB-03 | Product Information | Retrieve product title, price, short description, and context content | Product information displays clearly and matches the product data | Product title, price, short description, and context content displayed clearly and matched the product data | PASS | |
| PDB-04 | Product Breadcrumbs | Click breadcrumb links on the prduct detail page | Breadcrumb links return the user to the correct catalogue or collection page | Product breadcrumb links returned the user to the correct catalogue or collection page | PASS | |
| PDB-05 | Related Products | Review the related products section on a product detail page | Related products from the same collection display correctly | Related products from the same collection displayed correctly on the product detail page | PASS | |
| PDB-06 | Related Product Links | Click products from the related products section | Each related product opens the correct product detail page | Each related product link opened the correct product detail page | PASS | |
| PDB-07 | Add to Bag | Add a product to the bag using the Add to bag button | Product is added successfully and a confirmation message appears | Product was added to the bag successfully and a confirmation message appeared | PASS | |
| PDB-08 | Buy Now | Click the Buy now button on a product detail page | Product is added to the bag and the user is taken to the checkout flow or bag as intended | The Buy now button added the product successfully and followed the intended purchase flow | PASS | |
| PDB-09 | Bag Page Load | Open the bag page with one or more products added | Bag page loads correctly and displays selected products | The bag page loaded correctly and displayed the selected products | PASS | |
| PDB-10 | Bag Item Details | Review bag content | Bag shows the correct product image, title, price, and any relevant product information | The bag displayed the correct product image, title, price, and relevant product information | PASS | |
| PDB-11 | Bag Total Calculation | Add products and review bag totals | Bag totals calculate correctly based on the products added | Bag totals calculated correctly based on the products added | PASS | |
| PDB-12 | Multiple Product Additions | Add more than one product to the bag | All added products appear correctly in the bag and totals update correctly | Multiple added products appeared correctly in the bag and totals updated correctly | PASS | |
| PDB-13 | Remove From Bag | Remove a product from the bag | Product is successfully removed and totals update correctly | The selected product was removed successfully and bag totals updated correctly | PASS | |
| PDB-14 | Empty Bag State | Remove all products from the bag | Empty bag message and layout display correctly | The empty bag message and layout displayed correctly after all products were removed | PASS | |
| PDB-15 | Bag Navigation | Use bag page button such as Continue shopping and Proceed to checkout | Buttons route correctly to the intended pages | Continue shopping worked correctly, but the checkout button did not advance to the checkout page | FAIL | Checkout button on the bag page is not routing correctly to the checkout page and needs investigation |
| PDB-16 | Toast Messages | Add a product to the bag and observe toast/feedback messages | Clear success feedback appears and dismisses correctly | Clear success feedback appeared correctly after adding a product to the bag | PASS | |
| PDB-17 | Toast Dismiss | Manually close a toast message | Toast closes correctly without affecting page layout | The toast message closed correctly without affecting the page layout | PASS | |
| PDB-18 | Product Detail Desktop | Review product detail and bag pages on desktop viewport | Layout is clear, stable, and visually consistent on desktop | Product detail and bag pages remained clear, stable, and visually consistent on desktop | PASS | |
| PDB-19 | Product Detail Mobile | Review product detail and bag pages on mobile viewport | Layout is clear, stable, and visually consistent on mobile | Product detail and bag pages remained clear, stable, and visually consistent on mobile | PASS | |
| PDB-20 | Product Detail Tablet | Review product detail and bag pages on tablet viewport | Layout is clear, stable, and visually consistent on tablet | Product detail and bag pages remained clear, stable, and visually consistent on tablet | PASS | |
| PDB-21 | Product Image Loading | Review product images on product detail and bag pages | Images load correctly without distortion or broken paths | Product images loaded correctly on product detail and bag pages without distortion or broken paths | PASS | |
| PDB-22 | Superuser Product Actions | View product detail page as a superuser | Edit and delete product links appear only for authorised superuser users | Edit and delete product links appeared correctly for the superuser on the product detail page | PASS | |
| PDB-23 | Normal User Product Restrictions | View product detail page as a logged-out or normal user | Admin-only edit and delete links are visually hidden from unauthorised users | Admin-only edit and delete links were hidden from logged-out users and normal users | PASS | |

### Checkout and Order Flow

| Test ID | Feature | Test | Expected Result | Actual Result | Pass/Fail | Notes |
|---------|---------|------|-----------------|---------------|-----------|-------|
| CHK-01 | Checkout Page Load | Open the checkout page with products in the bag | Checkout page loads correctly with order summary, form fields, and payment section visible | | | |
| CHK-02 | Empty Bag Checkout Restriction | Attempt to open the checkout page with an empty bag | User is redirected away from the checkout page and shown an appropiate message | Attempting to access checkout with an empty bag redirected the user away from checkout and showed an appropriate message | PASS | |
| CHK-03 | Checkout Form Visibility | Review the checkout form fields and labels | All required checkout fields are visible, labelled clearly, and usable | | | |
| CHK-04 | Checkout Form Validation | Submit the checkout form with missing required fields | Form validation prevents submission and clear  erros messages are shown | | | |
| CHK-05 | Checkout Email Field | Submit checkout form with a vaid email address | Email field accepts valid input and order can proceed | | | |
| CHK-06 | Checkout Save Info Option | Complete checkout while selecting the save info option as an authenticated user | Profile information is saved to the user profile correctly | | | |
| CHK-07 | Guest Checkout | Compete checkout as a guest user | Guest user can place an order successfully without being required to log in | | | |
| CHK-08 | Authenticated Checkout | Complete checkout while logged in | Logged-in user can place an order successfully and the order is linked to their account | | | |
| CHK-09 | Stripe Payment Success | Complete a successful test payment through Stripe | Payment succeeds, order is created, and user is redirected to the checkout success page | | | |
| CHK-10 | Stripe Payment Failure | Trigger a failed or invalid test payment | Payment is rejected safely and the user is shown an appropiate error or prevented from completing checkout | | | |
| CHK-11 | Checkout Success Page | open the checkout success page after successful payment | Success page loads correctly with order number, customer details, and order summary | | | |
| CHK-12 | Success page Download Access | Review downloadable file links on the checkout success page | Purchased downloads are displayed correctly and are accessible from the success page | | | |
| CHK-13 | Download Purchased File | Click a valid purchased download link from the success page | Correct file downloads successfully | | | |
| CHK-14 | Download Restriction | Attempt to access a download that does not belong to the order | Access denied and file is not available to unauthorised users | | | |
| CHK-15 | Order Confirmation Message | Review successs message after completed checkout | Clear confirmation feedback is shown after the order is processed | | | |
| CHK-16 | Order Email Sent | Complete a successful order and check the customer inbox or mail output | Customer receives an order confirmation email with the correct order information | | | |
| CHK-17 | Order Data Accuracy | Compare checkout input with success page order data | Order details, billing details, and totals match the submitted order | | | |
| CHK-18 | Bag Clearance After Checkout | Complete a successful checkout and review the bag | Bag is cleared after successful order completion | | | |
| CHK-19 | Profile Order History | Complete a successful order as an authenticated user and review the profile | The new order appears correctly in the user's profile order history | | | |
| CHK-20 | Profile Download Access | Review purchased downloads from the profile area after checkout | Authenticated user can access purchased downloads from their account area | | | |
| CHK-21 | Checkout Desktop Layout | Review checkout and success pages on desktop viewport | Layout is clear, stable, and visually consistent on desktop | | | |
| CHK-22 | Checkout Mobile Layout | Review checkout and success pages on mobile viewport | Layout is clear, stable, and visually consistent on mobile | | | |
| CHK-23 | Checkout Tablet Layout | Review checkout and success pages on tablet viewport | Layout is clear, stable, and visually consistent on tablet | | | |
| CHK-24 | Webhook Order Handling | Complete a successful payment and confirm order processing works in deployed environment | Order is processed correctly and payment data is handled without errors | | | |
| CHK-25 | Save Info Session Cleanup | Complete a successful order and review session behaviour | Save info session data is cleared after the checkout flow completes | | | |
| CHK-26 | Stripe CLI Webhook Forwarding | Run Stripe locally, forward webhook eventsto the local webhook endpoint, and trigger a successful test event | Stripe webhook events are recieved by the local application and processed correctly, allowing local verification od webhook-based order handling | | | |

### Authentication and Profiles

| Test ID | Feature | Test | Expected Result | Actual Result | Pass/Fail | Notes |
|---------|---------|------|-----------------|---------------|-----------|-------|
| AUT-01 | Sign Up Page Load | Open the sign up page | Sign up page loads correctly with all required fields visible | The sign up page loaded correctly with all required fields visible | PASS | |
| AUT-02 | User Registration | Complete the sign up form with valid details | New user account is created successfully | The registration flow completed, but the production email backend logged emails to Heroku instead of sending them to a real inbox | FAIL | Production email backend is currently configured to log emails rather than send them to a real inbox |
| AUT-03 | Email Verification | Follow the email verification flow after signup | User receives verification email and can verify account | | | |
| AUT-04 | Duplicate Account Prevention | Attempt to sign up using an email that already exists | Duplicate registration is preveneted and user sees appropiate feedback | | | |
| AUT-05 | Login Page Load | Open the login page | Login page loads correctly with all required fields visible | The login page loaded correctly with all required fields visible | PASS | |
| AUT-06 | Valid Login | Log in using valid user credentials | User is authenticated successfully and redirected correctly | | | |
| AUT-07 | Invalid Login | Attempt to log in with invalid credentials | Login is rejected and clear feedback is shown | The login attempt was rejected, but the user was taken to the verification page instead of being shown clear invalid-credentials feedback | FAIL | Invalid login handling needs clearer user feedback. Users should be told that the credentials are incorrect and, if appropriate, be directed to sign up instead of being sent to the verification page |
| AUT-08 | Logout | Log out from an authenticated account | User is logged out successfully and redirected correctly | The user was logged out successfully and redirected correctly | PASS | |
| AUT-09 | Logged-Out Header/Footer State | Review account-related links while logged out | Login and account-related links display correctly for logged-out users | Account-related header and footer links displayed correctly for logged-out users | PASS | |
| AUT-10 | Logged-In Header/Footer State | Review account-related links while logged in | Profile, orders, and other account-related links display correctly for authenticated users | Account-related header and footer links displayed correctly for authenticated users | PASS | |
| AUT-11 | Profile Page Access | Open the profile page while logged in | Profile page loads correctly with user information and order history area | The profile page loaded correctly while logged in, with user information and the order history area visible | PASS | |
| AUT-12 | Profile Access Restriction | Attempt to open the profile page while logged out | Unauthorised user is redirected to login or blocked appropriately | Logged-out users were redirected or blocked appropriately when attempting to access the profile page | PASS | |
| AUT-13 | Profile Detail Display | Review saved profile details on the profile page | Profile information displays correctly and matches saved user data | | | |
| AUT-14 | Profile Update | Update profile information and save changes | Updated profile details are saved successfully | | | |
| AUT-15 | Save Info to Profile | Complete checkout with save info enabled, then review profile | Checkout billing details are saved correctly to the user profile | | | |
| AUT-16 | Profile Order History | Review the order history section as an authenticated user with completed orders | Previous orders display correctly in the profile order history | | | |
| AUT-17 | Profile Order Detail Link | Click an order from the profile order history if linked | User can access the correct order detail or order summary view | | | |
| AUT-18 | Profile Download Access | Review purchased downloads from the profile area | User can access valid downloads for purchased products | | | |
| AUT-19 | Download Access Restriction | Attempt to access downloads not belonging to the logged-in user's order | Unauthorised download access is prevented | | | |
| AUT-20 | Login Redirect for Orders | Click the Orders link while logged out | User is sent to login and can access orders only after authentication | Clicking the Orders link while logged out redirected the user to the login page as expected | PASS | |
| AUT-21 | Session Persistence | Log in and navigate between pages | User remains authenticated across normal site navigation | The user remained authenticated across normal site navigation after logging in | PASS | |
| AUT-22 | Authentication Desktop Layout | Review authentication profile pages on desktop viewport | Layout is clear, stable, and visually consistent on desktop | Authentication and profile pages remained clear, stable, and visually consistent on desktop | PASS | |
| AUT-23 | Authentication Mobile Layout | Review authentication profile pages on mobile viewport | Layout is clear, stable, and visually consistent on mobile | Authentication and profile pages remained clear, stable, and visually consistent on mobile | PASS | |
| AUT-24 | Authentication Tablet Layout | Review authentication profile pages on tablet viewport | Layout is clear, stable, and visually consistent on tablet | Authentication and profile pages remained clear, stable, and visually consistent on tablet | PASS | |
| AUT-25 | Superuser Access Separation | Log in as superuser and review normal profile/account behaviour | Superuser can still access normal account features while seeing admin-only controls where intended | The superuser could access normal account features while also seeing admin-only controls where intended | PASS | |

### Newsletter Signup

| Test ID | Feature | Test | Expected Result | Actual Result | Pass/Fail | Notes |
|---------|---------|------|-----------------|---------------|-----------|-------|
| NEW-01 | Footer Newsletter Form Visibility | Review the newsletter form in the site footer | Footer newsletter form is visible, styled correctly, and includes email field and submit button | The footer newsletter form was visible, styled correctly, and included an email field and submit button | PASS | |
| NEW-02 | Newsletter CTA Form Visibility | Review the dedicated newsletter CTA form on pages where it appears | Newsletter CTA form is visible, styled correctly, and includes email field and submit button | The newsletter CTA form was visible, styled correctly, and included an email field and submit button | PASS | |
| NEW-03 | Valid Footer Signup Submission | Submit the footer newsletter form with a valid email address | Newsletter signup succeeds and a clear success message is shown | Submitting a valid email address through the footer newsletter form triggered a server error 500 instead of completing successfully | FAIL | Footer newsletter signup is currently broken and returns a 500 server error on valid submission |
| NEW-04 | Valid CTA Signup Submission | Submit the newsletter CTA form with a valid email address | Newsletter signup succeeds and a clear success message is shown | | | |
| NEW-05 | Empty Email Validation | Submit a newsletter form without entering an email address | Form submission is prevented or validation message is shown for required email field | Newsletter form submission was prevented or validation feedback was shown when the email field was left empty | PASS | |
| NEW-06 | Invalid Email Validation | Submit a newsletter form with an invalid email format | Form validation prevents submission and clear feedback is shown | Newsletter form validation prevented submission and showed clear feedback for invalid email input | PASS | |
| NEW-07 | Duplicate Email Handling | Submit a newsletter form using an email address that is already subscribed | Duplicate subscription is handled correctly with appropriate feedback | | | |
| NEW-08 | Redirect Back to Origin Page | Submit a newsletter form from different pages of the site | User is returned to the correct page after submission | | | |
| NEW-09 | Success Message Display | Complete a valid newsletter signup | Success message appears clearly and matches expected site feedback pattern | | | |
| NEW-10 | Error Message Display | Submit invalid newsletter data | Clear and readable error feedback is displayed to the user | | | |
| NEW-11 | CSRF Protection | Submit newsletter form on local and deployed site | Form submits securely without CSRF errors when configured correctly | | | |
| NEW-12 | Footer Form Across Pages | Test the footer newsletter form from multiple pages | Footer form behaves consistently across the site | The footer newsletter form behaved consistently across the pages tested | PASS | |
| NEW-13 | CTA Form Across Pages | Test the newsletter CTA form from pages where it appears | CTA form behaves consistently across the site | The newsletter CTA form behaved consistently across the pages tested | PASS | |
| NEW-14 | Newsletter Form Desktop Layout | Review newsletter forms on desktop viewport | Form layout is clear, stable, and visually consistent on desktop | Newsletter forms remained clear, stable, and visually consistent on desktop | PASS | |
| NEW-15 | Newsletter Form Mobile Layout | Review newsletter forms on mobile viewport | Form layout is clear, stable, and visually consistent on mobile | Newsletter forms remained clear, stable, and visually consistent on mobile | PASS | |
| NEW-16 | Newsletter Form Tablet Layout | Review newsletter forms on tablet viewport | Form layout is clear, stable, and visually consistent on tablet | Newsletter forms remained clear, stable, and visually consistent on tablet | PASS | |
| NEW-17 | Field Accessibility | Review labels, focus states, and keyboard access for newsletter forms | Newsletter forms are keyboard accessible and include usable labels/focus states | Newsletter forms were keyboard accessible and included usable labels and focus states | PASS | |

### Product Admin

| Test ID | Feature | Test | Expected Result | Actual Result | Pass/Fail | Notes |
|---------|---------|------|-----------------|---------------|-----------|-------|
| ADM-01 | Add Product Page Access | Open the add product page as a superuser | Add product page loads correctly with the full form visible | The add product page loaded correctly for the superuser with the full form visible | PASS | |
| ADM-02 | Add Product Page Restriction | Attempt to access the add product URL as a logged-out user and as a normal authenticated user | Unauthorised users are redirected or blocked with appropriate feedback | Logged-out users and normal authenticated users were redirected or blocked appropriately from the add product page | PASS | |
| ADM-03 | Add Product From Catalogue | Click the Add product button on the catalogue page as a superuser | Add product page opens correctly from the catalogue UI | The Add product button on the catalogue page opened the add product page correctly for the superuser | PASS | |
| ADM-04 | Add Product From Collection Detail | Click the Add product button on a collection detail page as a superuser | Add product page opens correctly from the collection detail UI | The Add product button on the collection detail page opened the add product page correctly for the superuser | PASS | |
| ADM-05 | Add Product Button Restriction | View add product entry points as a logged-out user and as a normal authenticated user | Add product buttons are hidden from unauthorised users | Add product buttons were hidden from logged-out users and normal authenticated users | PASS | |
| ADM-06 | Product Form Visibility | Review the add/edit product form fields | All required product fields are visible, labelled clearly, and usable | All required product form fields were visible, clearly labelled, and usable | PASS | |
| ADM-07 | Product Slug Autofill | Type a product title into the title field on the add product page | Slug field auto-populates correctly unless manually edited | The slug field auto-populated correctly when a product title was entered | PASS | |
| ADM-08 | Add Product Validation | Submit the add product form with missing required fields | Form validation prevents submission and clear error messages are shown | Form validation prevented submission and displayed clear error messages for missing required fields | PASS | |
| ADM-09 | Add Product Success | Submit the add product form with valid data | Product is created successfully and redirects correctly | A valid product was created successfully and the user was redirected correctly | PASS | |
| ADM-10 | Product Appears in Catalogue | Create a valid active product and review the catalogue | New active product appears correctly in the catalogue | The new active product appeared correctly in the catalogue | PASS | |
| ADM-11 | Product Detail After Creation | Create a valid product and open its detail page | Product detail page displays the newly created product correctly | The newly created product displayed correctly on its product detail page | PASS | |
| ADM-12 | Edit Product Page Access | Open the edit product page as a superuser | Edit product page loads correctly with existing product data populated | The edit product page loaded correctly for the superuser with existing product data populated | PASS | |
| ADM-13 | Edit Product Restriction | Attempt to access edit product URLs as a logged-out user and as a normal authenticated user | Unauthorised users are redirected or blocked with appropriate feedback | Logged-out users and normal authenticated users were redirected or blocked appropriately from edit product URLs | PASS | |
| ADM-14 | Edit Product Success | Update product details and save changes | Product updates successfully and changes appear on the product detail page and catalogue where relevant | Product details updated successfully and the changes appeared correctly on the product detail page and in the catalogue where relevant | PASS | |
| ADM-15 | Delete Product Page Access | Open the delete product confirmation page as a superuser | Delete confirmation page loads correctly | The delete product confirmation page loaded correctly for the superuser | PASS | |
| ADM-16 | Delete Product Restriction | Attempt to access delete product URLs as a logged-out user and as a normal authenticated user | Unauthorised users are redirected or blocked with appropriate feedback | Logged-out users and normal authenticated users were redirected or blocked appropriately from delete product URLs | PASS | |
| ADM-17 | Delete Product Success | Confirm deletion of a product as a superuser | Product is deleted successfully and no longer appears in the catalogue | The product was deleted successfully and no longer appeared in the catalogue | PASS | |
| ADM-18 | Product Detail Admin Links | View a product detail page as a superuser | Edit and delete product links are visible and route correctly | Edit and delete product links were visible to the superuser and routed correctly | PASS | |
| ADM-19 | Product Detail Admin Link Restriction | View a product detail page as a normal user or logged-out user | Edit and delete product links are hidden from unauthorised users | Edit and delete product links were hidden from normal users and logged-out users | PASS | |
| ADM-20 | Product Image Form Visibility | Review the image management section on the edit product page | Image upload fields, alt text field, sort order, and primary image checkbox are visible and usable | Image upload fields, alt text, sort order, and the primary image checkbox were visible and usable in the image management section | PASS | |
| ADM-21 | Add Product Image | Upload a valid product image | Image is added successfully and appears in the image management list and relevant product displays | A valid product image was added successfully and appeared in the image management list and relevant product displays | PASS | |
| ADM-22 | Edit Product Image | Update product image alt text, sort order, or primary status | Image changes save successfully and display correctly | Product image alt text, sort order, and primary status updated successfully and displayed correctly | PASS | |
| ADM-23 | Delete Product Image | Delete a product image from the edit product page | Image is removed successfully and no longer appears on the product | The product image was deleted successfully and no longer appeared on the product | PASS | |
| ADM-24 | Primary Image Logic | Mark one image as primary when other images already exist | Only one product image remains marked as primary at a time | Only one product image remained marked as primary when another image was set as primary | PASS | |
| ADM-25 | Product Download Form Visibility | Review the downloadable file management section on the edit product page | Download title, file input, and sort order fields are visible and usable | | | |
| ADM-26 | Add Product Download | Upload a valid downloadable file to a product | Download file is added successfully and appears in the product download management section | | | |
| ADM-27 | Edit Product Download | Update download title or sort order for an existing file | Download details update successfully | | | |
| ADM-28 | Delete Product Download | Delete an existing downloadable file from a product | Download file is removed successfully | | | |
| ADM-29 | Download Availability After Purchase | Purchase a product with an uploaded download file | Uploaded file is available to the buyer on checkout success/profile as expected | | | |
| ADM-30 | Inactive Product Behaviour | Create or edit a product so that it is inactive | Inactive product does not appear in public catalogue views | Inactive products did not appear in public catalogue views | PASS | |
| ADM-31 | Featured Product Behaviour | Mark a product as featured | Featured product appears correctly in featured areas if applicable | The featured product appeared correctly in the relevant featured areas | PASS | |
| ADM-32 | Product Admin Desktop Layout | Review add/edit/delete product admin pages on desktop viewport | Layout is clear, stable, and visually consistent on desktop | Product admin add, edit, and delete pages remained clear, stable, and visually consistent on desktop | PASS | |
| ADM-33 | Product Admin Mobile Layout | Review add/edit/delete product admin pages on mobile viewport | Layout remains usable and visually consistent on mobile | Product admin add, edit, and delete pages remained usable and visually consistent on mobile | PASS | |
| ADM-34 | Product Admin Tablet Layout | Review add/edit/delete product admin pages on tablet viewport | Layout remains usable and visually consistent on tablet | Product admin add, edit, and delete pages remained usable and visually consistent on tablet | PASS | |

### Media and Static Files

| Test ID | Feature | Test | Expected Result | Actual Result | Pass/Fail | Notes |
|---------|---------|------|-----------------|---------------|-----------|-------|
| MED-01 | Global CSS Load | Open major pages on the deployed site | Global CSS loads correctly and pages display styled layouts rather than unstyled HTML | Global CSS loaded correctly and major pages displayed styled layouts rather than unstyled HTML | PASS | |
| MED-02 | Global JavaScript Load | Open major pages and test interactive elements | JavaScript loads correctly and interactive features work as expected | JavaScript loaded correctly and interactive features worked as expected on the pages tested | PASS | |
| MED-03 | Logo Assets | Review header and footer branding images | Logo assets load correctly without distortion or broken paths | Header and footer logo assets loaded correctly without distortion or broken paths | PASS | |
| MED-04 | Homepage Static Images | Review all homepage static images | Homepage images load correctly and display at the intended sizes | Homepage static images loaded correctly and displayed at the intended sizes | PASS | |
| MED-05 | Catalogue Static Images | Review static images on the catalogue page | Catalogue page static images load correctly and display at the intended sizes | Catalogue page static images loaded correctly and displayed at the intended sizes | PASS | |
| MED-06 | Collections Static Images | Review static images on the collections page | Collections page static images load correctly and display at the intended sizes | Collections page static images loaded correctly and displayed at the intended sizes | PASS | |
| MED-07 | About Page Static Images | Review all About page static images | About page images load correctly and display at the intended sizes | About page static images loaded correctly and displayed at the intended sizes | PASS | |
| MED-08 | Product Media Images | Review uploaded product images in catalogue, product detail, bag, and admin views | Product media loads correctly without broken paths or distortion | Uploaded product images loaded correctly in catalogue, product detail, bag, and admin views without broken paths or distortion | PASS | |
| MED-09 | Collection Media Images | Review uploaded collection images in collection list and collection detail views | Collection media loads correctly without broken paths or distortion | Uploaded collection images loaded correctly in collection list and collection detail views | PASS | |
| MED-10 | Narrative Panel Images | Review uploaded collection narrative panel images | Narrative panel images load correctly and display in the correct sections | Narrative panel images loaded correctly and displayed in the correct sections | PASS | |
| MED-11 | Image Aspect Ratios | Review images across key pages | Images maintain correct cropping, sizing, and aspect ratio behaviour | Image aspect ratios were not fully consistent across key pages, with product detail thumbnails showing inconsistent proportions | FAIL | Product detail page thumbnail aspect ratios need to be standardised for a more consistent gallery presentation |
| MED-12 | Static File Paths in Production | Review deployed site assets through page inspection or browser tools | Static file URLs resolve correctly in production without 404 asset errors | Static file URLs resolved correctly in production without 404 asset errors | PASS | |
| MED-13 | Media File Paths in Production | Review uploaded media on the deployed site | Media file URLs resolve correctly in production without broken file links | Uploaded media file URLs resolved correctly in production without broken file links | PASS | |
| MED-14 | Font Loading | Review typography on deployed pages | Fonts load correctly and fallback issues are not visible | Fonts loaded correctly and no fallback issues were visible | PASS | |
| MED-15 | Font Awesome Icons | Review icon usage such as footer social icons and bag/account icons | Icons load correctly and display as intended | Icons loaded successfully, but the bag icon styling was inconsistent and did not visually align with the other header icons | FAIL | Icon asset loads correctly, but header icon styling needs adjustment for colour consistency and alignment |
| MED-16 | File Download Delivery | Download a purchased product file from success page or profile | Downloaded file is served correctly and matches the uploaded asset | | | |
| MED-17 | Static Files on Mobile | Review core pages on mobile viewport | Static images and assets load correctly on mobile without layout breakage | Static images and assets loaded correctly on mobile without layout breakage | PASS | |
| MED-18 | Static Files on Tablet | Review core pages on tablet viewport | Static images and assets load correctly on tablet without layout breakage | Static images and assets loaded correctly on tablet without layout breakage | PASS | |
| MED-19 | Static Files on Desktop | Review core pages on desktop viewport | Static images and assets load correctly on desktop without layout breakage | Static images and assets loaded correctly on desktop without layout breakage | PASS | |
| MED-20 | Missing Asset Check | Review major pages for broken image icons, missing files, or visible path issues | No broken assets or missing media are visible on public-facing pages | A missing asset was visible on the collection detail page | FAIL | |

### Responsive Testing

| Test ID | Feature | Test | Expected Result | Actual Result | Pass/Fail | Notes |
|---------|---------|------|-----------------|---------------|-----------|-------|
| RES-01 | Homepage Mobile Layout | Review the homepage on a mobile viewport | Homepage layout remains readable, usable, and visually consistent on mobile | The homepage layout remained readable, usable, and visually consistent on mobile | PASS | |
| RES-02 | Homepage Tablet Layout | Review the homepage on a tablet viewport | Homepage layout remains readable, usable, and visually consistent on tablet | The homepage layout remained readable, usable, and visually consistent on tablet | PASS | |
| RES-03 | Homepage Desktop Layout | Review the homepage on a desktop viewport | Homepage layout remains readable, usable, and visually consistent on desktop | The homepage layout remained readable, usable, and visually consistent on desktop | PASS | |
| RES-04 | Static Pages Mobile | Review About, Contact, FAQ, and policy pages on mobile | Static content pages remain readable and usable on mobile | Static content pages remained readable and usable on mobile | PASS | |
| RES-05 | Static Pages Tablet | Review About, Contact, FAQ, and policy pages on tablet | Static content pages remain readable and usable on tablet | Static content pages remained readable and usable on tablet | PASS | |
| RES-06 | Catalogue Mobile | Review catalogue and collection list/detail pages on mobile | Product grids, filters, cards, and images remain usable on mobile | Catalogue and collection pages remained usable on mobile, with grids, filters, cards, and images displaying correctly | PASS | |
| RES-07 | Catalogue Tablet | Review catalogue and collection list/detail pages on tablet | Product grids, filters, cards, and images remain usable on tablet | Catalogue and collection pages remained usable on tablet with stable grids, cards, filters, and images | PASS | |
| RES-08 | Product Detail Mobile | Review product detail page on mobile | Product gallery, text, price, and buttons remain usable on mobile | The product detail page remained usable on mobile, but the main image aspect ratio was not consistent with the additional thumbnails | FAIL | Product image gallery needs aspect ratio consistency between the main image and thumbnails on mobile |
| RES-09 | Product Detail Tablet | Review product detail page on tablet | Product gallery, text, price, and buttons remain usable on tablet | The product detail page remained usable on tablet, but the main image aspect ratio was not consistent with the additional thumbnails | FAIL | Product image gallery needs aspect ratio consistency between the main image and thumbnails on tablet |
| RES-10 | Bag and Checkout Mobile | Review bag and checkout pages on mobile | Bag summary, checkout form, and buttons remain usable on mobile | Bag and checkout pages remained usable on mobile | PASS | |
| RES-11 | Bag and Checkout Tablet | Review bag and checkout pages on tablet | Bag summary, checkout form, and buttons remain usable on tablet | Bag and checkout pages remained usable on tablet | PASS | |
| RES-12 | Authentication Mobile | Review sign up, login, and profile pages on mobile | Authentication and profile pages remain usable and readable on mobile | Authentication and profile pages remained usable and readable on mobile | PASS | |
| RES-13 | Authentication Tablet | Review sign up, login, and profile pages on tablet | Authentication and profile pages remain usable and readable on tablet | Authentication and profile pages remained usable and readable on tablet | PASS | |
| RES-14 | Product Admin Mobile | Review add/edit/delete product admin pages on mobile | Product admin pages remain usable and readable on mobile | Product admin pages remained usable and readable on mobile | PASS | |
| RES-15 | Product Admin Tablet | Review add/edit/delete product admin pages on tablet | Product admin pages remain usable and readable on tablet | Product admin pages remained usable and readable on tablet | PASS | |
| RES-16 | Navigation Mobile | Test header, mobile menu, footer links, and key CTAs on mobile | Navigation remains accessible and functional on mobile | Mobile navigation remained accessible and functional across header, mobile menu, footer links, and key CTAs | PASS | |
| RES-17 | Navigation Tablet | Test header, footer links, and key CTAs on tablet | Navigation remains accessible and functional on tablet | Header, footer links, and key CTAs remained accessible and functional on tablet | PASS | |
| RES-18 | Buttons and CTAs | Review buttons and CTA groups across breakpoints | Buttons remain readable, clickable, and correctly aligned across screen sizes | Buttons and CTA groups remained readable, clickable, and correctly aligned across screen sizes | PASS | |
| RES-19 | Forms Across Breakpoints | Review newsletter, contact, checkout, auth, and admin forms across breakpoints | Forms remain readable, aligned, and usable across screen sizes | Forms remained readable, aligned, and usable across the breakpoints tested | PASS | |
| RES-20 | Images Across Breakpoints | Review static and uploaded images across screen sizes | Images scale correctly without distortion, overflow, or broken layout | Images scaled correctly across screen sizes without distortion, overflow, or broken layout | PASS | |
| RES-21 | Typography Across Breakpoints | Review headings, body text, and spacing across screen sizes | Typography remains readable and hierarchy remains clear across breakpoints | Typography remained readable and hierarchy remained clear across breakpoints | PASS | |
| RES-22 | No Horizontal Scrolling | Review major pages on mobile and tablet | No unintended horizontal scrolling occurs | No unintended horizontal scrolling occurred on the pages tested on mobile and tablet | PASS | |
| RES-23 | No Overlap or Clipping | Review major layouts across breakpoints | Content does not overlap, clip, or disappear at smaller sizes | Content did not overlap, clip, or disappear at the breakpoints tested | PASS | |
| RES-24 | Toast/Message Behaviour | Trigger toast messages on mobile and tablet | Toasts display clearly without covering critical UI or breaking layout | Toast messages displayed clearly on mobile and tablet without breaking the layout | PASS | |
| RES-25 | Responsive Consistency | Review overall experience across mobile, tablet, and desktop | Visual style and usability remain consistent across breakpoints | Visual style and usability remained consistent across mobile, tablet, and desktop | PASS | |

### Error Handling

| Test ID | Feature | Test | Expected Result | Actual Result | Pass/Fail | Notes |
|---------|---------|------|-----------------|---------------|-----------|-------|
| ERR-01 | Custom 404 Page | Open a clearly invalid URL on the deployed site | Custom 404 page displays correctly with site styling and helpful navigation options | The custom 404 page displayed correctly with site styling and helpful navigation options | PASS | |
| ERR-02 | Custom 403 Page | Attempt to access a restricted page without permission | Custom 403 page or appropriate restricted access response is shown | | | |
| ERR-03 | Custom 500 Page | Trigger or simulate a server error in a safe test scenario | Custom 500 page displays correctly in production when applicable | The custom 500 page displayed correctly in production when a server error was triggered in a safe test scenario | PASS | |
| ERR-04 | Empty Bag Checkout Protection | Attempt to access checkout with an empty bag | User is redirected appropriately and shown a helpful error or warning message | Attempting to access checkout with an empty bag redirected the user appropriately and showed a helpful message | PASS | |
| ERR-05 | Invalid Newsletter Submission | Submit newsletter form with invalid or missing email | Submission is blocked and clear validation feedback is shown | Invalid newsletter submission was blocked and clear validation feedback was shown | PASS | |
| ERR-06 | Invalid Contact Form Submission | Submit contact form with missing required fields or invalid data | Submission is blocked and clear validation feedback is shown | Invalid contact form submission was blocked and clear validation feedback was shown | PASS | |
| ERR-07 | Invalid Login Attempt | Submit incorrect login credentials | Login fails safely and clear feedback is displayed | | | |
| ERR-08 | Duplicate Signup Attempt | Attempt to register with an email that already exists | Duplicate account creation is prevented and clear feedback is displayed | | | |
| ERR-09 | Product Admin Access Restriction | Attempt to access add, edit, or delete product URLs as a logged-out or non-superuser user | User is blocked or redirected with appropriate feedback | Unauthorised users were blocked or redirected with appropriate feedback when attempting to access restricted product admin URLs | PASS | |
| ERR-10 | Product Image Admin Restriction | Attempt to access product image add, edit, or delete URLs without superuser access | User is blocked or redirected with appropriate feedback | Unauthorised users were blocked or redirected with appropriate feedback when attempting to access restricted product image admin URLs | PASS | |
| ERR-11 | Product Download Admin Restriction | Attempt to access product download add, edit, or delete URLs without superuser access | User is blocked or redirected with appropriate feedback | Unauthorised users were blocked or redirected with appropriate feedback when attempting to access restricted product download admin URLs | PASS | |
| ERR-12 | Invalid Product Form Submission | Submit add/edit product form with invalid or missing required fields | Form is not submitted and clear validation errors are shown | Invalid product form submissions were blocked and clear validation errors were displayed | PASS | |
| ERR-13 | Invalid Image Upload Submission | Submit product image form with invalid or incomplete data | Form is not submitted and clear validation errors are shown | Invalid image upload submissions were blocked and clear validation errors were displayed | PASS | |
| ERR-14 | Invalid Download Upload Submission | Submit product download form with invalid or incomplete data | Form is not submitted and clear validation errors are shown | | | |
| ERR-15 | Missing Search Results | Search catalogue using a term with no matching products | Page remains stable and shows a clear no-results message | The catalogue remained stable and showed a clear no-results message when no products matched the search term | PASS | |
| ERR-16 | Missing Filter Results | Apply a filter that returns no matching products | Page remains stable and shows a clear empty-state message | | | |
| ERR-17 | Invalid Download Access | Attempt to open a download link that does not belong to the current user or order | Access is denied safely and file is not served | | | |
| ERR-18 | Failed Stripe Payment | Attempt checkout with an invalid or declined test payment method | Payment fails safely and user sees clear feedback without creating an incorrect completed order | | | |
| ERR-19 | Broken Asset Check | Review major pages for broken images, icons, CSS, or JS assets | No broken assets appear; if an asset fails, the page remains stable and usable | No broken assets were visible on the major pages tested, and pages remained stable and usable | PASS | |
| ERR-20 | Message Display Consistency | Trigger success, info, warning, and error messages where available | Site messages display clearly, dismiss correctly, and do not break layout | Site messages displayed clearly, dismissed correctly, and did not break page layout where tested | PASS | |

## User Story Testing

### US01

**User Story**  
As a visitor, I want to land on a clear homepage, so that I can quickly understand what Cities Under Watch is and what it sells.

**Acceptance Criteria**
- The homepage clearly introduces the brand and product offer
- The homepage includes clear paths to browse products or collections
- The homepage works well on mobile and desktop

**Test Performed**
- Opened the homepage on desktop
- Reviewed hero heading, supporting copy, and homepage sections
- Clicked the main Shop and Browse calls to action
- Checked layout and usability on mobile and desktop screen sizes

**Expected Result**
- The homepage clearly communicates the purpose of the site
- Users can easily navigate to products or collections
- The page is responsive and usable across device sizes

**Actual Result**
- The homepage clearly introduced the Cities Under Watch brand and explained the dystopian digital poster offer.
- The Shop and Browse calls to action linked correctly to the catalogue and collection pages.
- The homepage layout, imagery, and buttons remained clear and usable on both desktop and mobile screen sizes.

**Pass/Fail**
- Pass

**Notes**
- Tested on local and depolyed versions.

## Validation

| Test Area | Tool Used | Result | Notes |
|----------|-----------|--------|-------|
| HTML | W3C HTML Validator | | |
| CSS | W3C CSS Validator | | |
| JavaScript | JSHint | | |
| Python | Python/flake8 | | |

### HTML Validation
### CSS Validation
### JavaScript Validation
### Python Validation

## Accessibility Testing

## Lighthouse Testing

| Page | Performance | Accessibility | Best Practices | SEO | Notes |
|------|-------------|---------------|----------------|-----|-------|
| Home | | | | | |

## Bugs Found and Fixed

| Bug | Cause | Fix | Status |
|-----|-------|-----|--------|
| Newsletter form 403 error | CSRF handling/form setup issue | Added correct CSRF token and submission route | Fixed |

## Known Issues