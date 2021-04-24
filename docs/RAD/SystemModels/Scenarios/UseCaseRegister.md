##### UseCaseRegister

***Participating Actors***

Initiated by Star.

***Entry Condition***

1. Star needs to sign up for an account and opens the ScreenRegisterEmail.

***Flow of Events***

1. Star enters his email.
1. WikiSpyWebsite checks if email is registered and if it is not then loads the ScreenRegisterUser that includes instructions on how to formulate a valid password.
1. Star enters in his password according to the password rules in two input fields along with his real name.
1. WikiSpyWebsite verifies the passwords match the password rules, the name doesn't contain invalid characters, sends Star a verification email to the email Star inputed in Step 1, and loads the ScreenRegistrationVerifyByEmail.
1. Star exits the browser window to check his email.

***Exit condition***

1. Star closes the web browser.

***Quantity Requirements***

* What are the min and max bounds?

***Navigation***

* [Requirements Analysis Document](../../)
   *  [System Models](../)
      * [Scenarios](./)
         * UseCaseRegister

## License

Copyright © 2020-1 [Kabuki Starship](https://kabukistarship.com).

This source code form is an open-source document, the Writings and Discoveries, that was written by and contains intellectual property belonging to the IP Owner. The Writings and Discoveries consist of documents, files, source code, technology design files, art, trademarks, and other content contained this file, folder and the GitHub repository, the Repo, located at <https://github.com/WikiSpy/WikiSpy>. The Writings and Discoveries are published under the Kabuki Strong Source-available License, the License, which is a non-commercial open-source license and is for educational and demonstration purposes only. To use the Writings and Discoveries for commercial purposes, you must download the Writings and Discoveries from <https://wikispy.us> and you will be bound to the license agreed upon before downloading the Writings and Discoveries. You may use, reproduce, publicly display, and modify the Writings and Discoveries so long as you submit and donate fixes and derived intellectual property, the Donated Ideas, to the Repo as an Issue ticket to become part of the Writings and Discoveries. You may not sell the Writings and Discoveries or otherwise profit from derivative works created from the Writings and Discoveries without the expressed written permission of the copyright holder. Unless required by applicable law or agreed to in writing, the Writings and Discoveries distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
