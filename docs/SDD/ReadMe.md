# WikiSpy Software Design Document

***Content Table***

1. [Introduction](./Introduction)
   2. [System Purpose](./Introduction/SystemPurpose.md)
   3. [Design Goals](./Introduction/DesignGoals.md)
   4. [Definitions](./Introduction/Definitions.md)
   5. [References](./Introduction/References.md)
   6. [Overview](./Introduction/Overview.md)
2. [Current Software Architecture](./CurrentSoftwareArchitecture)
3. [Proposed Software Architecture](./ProposedSoftwareArchitecture)
   1. [Overview](./ProposedSoftwareArchitecture/Overview.md)
   2. [Subsystem Decomposition](./ProposedSoftwareArchitecture/SubsystemDecomposition.md)
   3. [Hardware to Software Mapping](./ProposedSoftwareArchitecture/HardwareToSoftwareMapping.md)
   4. [Persistent Data Management](./ProposedSoftwareArchitecture/PersistentDataManagement.md)
   5. [Access Control and Security](./ProposedSoftwareArchitecture/AccessControlAndSecurity.md)
   6. [Global Software Control](./ProposedSoftwareArchitecture/GlobalSoftwareControl.md)
   7. [Boundary Conditions](./ProposedSoftwareArchitecture/BoundaryConditions.md)
4. [Subsystem Services](./SubsystemServices.md)
5. [Glossary](./Glossary.md)

## License

Copyright © 2020-1 [Kabuki Starship](https://kabukistarship.com).

This source code form is an open-source document, the Writings and Discoveries, that was written by and contains intellectual property belonging to the IP Owner. The Writings and Discoveries consist of documents, files, source code, technology design files, art, trademarks, and other content contained this file, folder and the GitHub repository, the Repo, located at <https://github.com/WikiSpy/WikiSpy>. The Writings and Discoveries are published under the Kabuki Strong Source-available License, the License, which is a non-commercial open-source license and is for educational and demonstration purposes only. To use the Writings and Discoveries for commercial purposes, you must download the Writings and Discoveries from <https://wikispy.us> and you will be bound to the license agreed upon before downloading the Writings and Discoveries. You may use, reproduce, publicly display, and modify the Writings and Discoveries so long as you submit and donate fixes and derived intellectual property, the Donated Ideas, to the Repo as an Issue ticket to become part of the Writings and Discoveries. You may not sell the Writings and Discoveries or otherwise profit from derivative works created from the Writings and Discoveries without the expressed written permission of the copyright holder. Unless required by applicable law or agreed to in writing, the Writings and Discoveries distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
