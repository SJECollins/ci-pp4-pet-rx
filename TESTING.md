# Testing


## [HTML Validator](https://validator.w3.org/)

HTML was validated by copying the page source and pasting into the validator.

- <details>
  <summary>Index Results</summary>

    ![Index results](readme-docs/testing/index-html-val.webp)
  </details>

- <details>
  <summary>About Results</summary>

  ![About results](readme-docs/testing/about-html-val.webp)
  </details>

- <details>
  <summary>Contact Results</summary>

  ![Contact results](readme-docs/testing/ontact-html-val.webp)
  </details>

- <details>
  <summary>Register Results</summary>

  ![Register results](readme-docs/testing/register-html-val.webp)
  </details>

- <details>
  <summary>Login Results</summary>

  ![Login results](readme-docs/testing/login-html-val.webp)
  </details>

- <details>
  <summary>Records Results</summary>

  ![Records results](readme-docs/testing/records-html-val.webp)
  </details>

- <details>
  <summary>Record Search Results</summary>

  ![Record Search results](readme-docs/testing/record-search-html-val.webp)
  </details>

- <details>
  <summary>Animal Record Results</summary>

  ![Animal Record results](readme-docs/testing/animal-record-html-val.webp)
  </details>

- <details>
  <summary>Add Animal Record Results</summary>

  ![Add Animal Record results](readme-docs/testing/add-animal-html-val.webp)
  </details>

- <details>
  <summary>Edit Animal Record Results</summary>

  ![Edit Animal Record results](readme-docs/testing/edit-animal-html-val.webp)
  </details>

- <details>
  <summary>Profile Results</summary>

  ![Profile results](readme-docs/testing/profile-html-val.webp)
  </details>

- <details>
  <summary>Edit Profile Results</summary>

  ![Edit Profile results](readme-docs/testing/edit-profile-html-val.webp)
  </details>

- <details>
  <summary>Drugs Results</summary>

  ![Drugs results](readme-docs/testing/drugs-html-val.webp)
  </details>

- <details>
  <summary>Drug Search Results</summary>

  ![Drug Search results](readme-docs/testing/drug-search-html-val.webp)
  </details>

- <details>
  <summary>Detailed Drug View Results</summary>

  ![Detail Drug View results](readme-docs/testing/detail-drug-html-val.webp)
  </details>


## [CSS Validator](https://jigsaw.w3.org/css-validator/)

CSS was validated by copying the CSS file into the validator.

- Results for style.css:
  - ![CSS results](readme-docs/testing/css-validator.webp)
  - <p>
        <a href="http://jigsaw.w3.org/css-validator/check/referer">
          <img style="border:0;width:88px;height:31px" src="http://jigsaw.w3.org/css-validator/images/vcss-blue" alt="Valid CSS!">
          </a>
      </p>


## JavaScript Testing

JSHint was used for validating the JavaScript for the modals and email. 


## Python Testing

The project was tested for pep8 compliance using pycodestyle. [autopep8](https://pypi.org/project/autopep8/) was used to aid compliance. # noqa was used in a small number of cases where necessary. At time of writing no problems or errors were found.


## Lighthouse
<summary>Example Title</summary>

![Title](readme-docs/)
</details>

<summary>Example Title</summary>

![Title](readme-docs/)
</details>

<summary>Example Title</summary>

![Title](readme-docs/)
</details>

<summary>Example Title</summary>

![Title](readme-docs/)
</details>

<summary>Example Title</summary>

![Title](readme-docs/)
</details>


## Automated Testing


## Manual Testing

Below the steps for manual testing of the site have been arranged into tables. User stories which were fulfilled can be matched by their keys in the next section.

<details>
<summary>Testing Registration & Login</summary>

![Testing Registration & Login](readme-docs/testing/testing-registration-login.png)
</details>

<details>
<summary>Testing VetProfiles</summary>

![Testing VetProfiles](readme-docs/testing/testing-vetprofiles.png)
</details>

<details>
<summary>Testing Records</summary>

![Testing Records](readme-docs/testing/testing-records.png)
</details>

<details>
<summary>Testing Prescriptions</summary>

![Testing Prescriptions](readme-docs/testing/testing-prescriptions.png)
</details>

<details>
<summary>Testing Admin</summary>

![Testing Admin](readme-docs/testing/testing-prescriptions.png)
</details>


## User Story Testing

The user stories were tested as part of the manual testing above and can be matched by their key.

- US1:
  - As a site user I can register on the site so that have access to the features for animal profiles and prescriptions
- US2:
  - As a site user I can edit my profile so that I can change my registered name or email
- US3:
  - As a site user I can create a new animal profile so that register a new animal's details in the database
- US4:
  - As a site user I can search so that I can find an individual animal's record
- US5:
  - As a site user I can view an animal's entry so that I can check their details on the database
- US6:
  - As a site user I can edit an animal's entry so that I can update their details on the database
- US7:
  - As a site user I can create a new prescription so that I can prescribe a medication to an animal and have it linked to their details on the database
- US8:
  - As a site user I can get a calculated dose for tablets so that I don't have to calculate tablets myself and the prescription will be accurately recorded
- US9:
  - As a site user I can filter drugs by category when adding a prescription so that I can find drugs more easily
- US10:
  - As a site user I can update an existing prescription so that changes I made are reflected in the database
- US11:
  - As a site user I can delete a prescription so that it is removed from the animal's record if it was incorrectly added
- US12:
  - As a site user I can view a list of the drugs available on the system so that I can see which drugs are available to prescribe
- US13:
  - As a site user I can search the drugs available on the system so that I can find a specific drug I may be looking for
- US14:
  - As a site user I can go to a detailed view of a drug so that I can review the details of the drug (eg, dose, warnings)
- US15:
  - As a site user I can view a list of previous prescriptions on an animal's profile so that I can review their previous prescriptions
- US16:
  - As a site user I can view a list of my previous prescriptions on my profile so that I can review the previous prescriptions I have created
- US17:
  - As a site user I can go to a detailed view of a prescription so that I can review the details of a prescription
- US18:
  - As a site admin I can add a medication so that site user's may prescribe it
- US19:
  - As a site admin I can edit a medication so that I can change the details of the prescription drug
- US20:
  - As a site admin I can delete a medication so that it can no longer be prescribed
- US21:
  - As a site admin I can delete a user profile so that they are no longer able to access the site


## Browser Compatibility
The website was tested on:
- Chrome Version 101.0.4951.67
- Firefox Version 101.0.4951.67
- Edge Version 101.0.1210.53
- Safari iOS Version 15.4.1


## Bugs

### Fixed Bugs

- Mobile Layout - Modals:
  - **Issue:** on small screens, some modals took up entire screen preventing closing.
  - **Description:** On larger screens, it was possible to close modals that don't have close buttons by tapping elsewhere on the screen. However, certain modals (e.g. adding prescription) were too large on a mobile screen to be able to tap away if a suer changes their mind and wants to back out.
  - **Fix:** add close button to all modals.


- Mobile Layout - User Email:
  - **Issue:** long user emails cause layout shifts.
  - **Description:** On very small screen sizes, the email displayed in the user's profile causes the page layout to break.
  - **Fix:** add "text-break" Bootstrap class.


- Contact Form - No Feedback:
  - **Issue:** no feedback when message sent from form.
  - **Description:** On initial deploy of live site, form was sending message but giving user no feedback - form not refreshing and no success message displayed. Accidentaly included form.save(), which is a not a valid method for a Form class and no necessary.
  - **Fix:** remove form.save()


- Tablet Calculation:
  - **Issue:** tablet doses not calculating correctly.
  - **Description:** Tablet doses are intended to calculate the smallest amount of a tablet in quarters. The intention is to making administration as easy as possible.
  For example, a 12.5kg dog requires a dose between 156.26mg and 187.5mg of amoxicillin clavunate. Assuming the clinic stocks 50mg, 250mg, and 500mg tablets (which are easily quartered), the dog may be prescribed either 3.25 x 50mg tablets (162.5mg) or 0.75 x 250mg tablets (187.5mg). 
  
    The prescription model's save function should have chosen 0.75mg, but instead was picking 3.5 x 50mg tablets. This is a perfectly valid dose, but not the smallest amount of quarters or even the smallest dose for that strength.
  Two things were happening related to Python's range() function: range works with integers, not floats, and range stops at -1.
  ![Tablet Error](readme-docs/testing/tab-error.webp)
  *The above image shows the incorrect dosage pre-fix (bottom) and the corrected dosage post-fix (top)*
  - **Fix:** To fix the first issue, the doses were multiplied by 100 and converted to integers, and the strengths multiplied by 25 for the calculation.
  
    To fix the second issue, +1 was added to the high dose.


### Known Bugs

There are currently no known bugs.