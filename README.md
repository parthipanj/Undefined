<h1>API-Style-Guide Overview</h1>

<table style="border: none;"><tr><td width="60%" valign="top">The Foo ecosystem is a collection of reusable services that encapsulate well-defined business capabilities. Developers are encouraged to access these capabilities through Application Programming Interfaces (APIs) that enable consistent design patterns and principles.
<br><br>
Foo APIs follow the RESTful architectural style as much as possible.<br><br>
Foo has adopted a set of industry rules, standards, and conventions that apply to the design of RESTful APIs
The primary purpose of this style guide is to ensure that Foo RESTful APIs can be easily and consistently * consumed by any client with basic HTTP support.<br><br>
These guidelines are applicable to any REST API exposed privately or publicly by Foo or any partner service
APIs SHOULD be developed with the intent that they will be exposed externally<br><Br>

There are legitimate reasons for exemption from these guidelines. For example, a REST service that implements or must
interoperate with some externally defined REST API must be compatible with that API and not necessarily these
guidelines. Some services MAY also have special performance needs that require a different format, such as a binary
protocol. Document Semantics, Formatting, and Naming
<br><br>
The keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "
OPTIONAL" in this document are to be interpreted as described
in <a href="https://www.ietf.org/rfc/rfc2119.txt" target="_blank">RFC 2119</a>.<br><br>
URIs containing variable blocks are specified according
to <a href="https://tools.ietf.org/html/rfc6570" target="_blank">URI Template RFC 6570</a>

<h2>Requesting an Update to the API Style Guide</h2>
The API Style Guide is comprised of Wiki Content within this GitHub Repository. All the Wiki Content is saved in GitHub
Files that can be found here:

To request an update:
<li> Fork this GitHub Repository </li>
<li> Copy the file contents you want to modify </li>
<li> If this is a brand new section, create a new File </li>
<li> Paste the file contents into a Wiki Section </li>
<li> Modify the Wiki as desired </li>
<li> Save your file contents back into GitHub </li>
<li> Submit a pull request to the source Repo </li>

</td> <td valign="top"><h3>Navigation</h3>
<a href="https://github.com/parthipanj/kissflow-xg/tree/master/APIStyleGuide/wiki/An-Overview-of-API-Design-Rules">An Overview of API Design and Rules</a><br>
<a href="https://github.com/parthipanj/kissflow-xg/API-Style-Guide/wiki/Styling-for-Security">Styling for Security</a><br>
<a href="https://github.com/parthipanj/kissflow-xg/API-Style-Guide/wiki/URL-Structure">URL Structure</a><br>
<a href="https://github.com/parthipanj/kissflow-xg/API-Style-Guide/wiki/HTTP-Headers">HTTP Headers</a><br>
<a href="https://github.com/parthipanj/kissflow-xg/API-Style-Guide/wiki/HTTP-Methods">HTTP Methods</a><br>
<a href="https://github.com/parthipanj/kissflow-xg/API-Style-Guide/wiki/HTTP-Status-Codes">HTTP Status Codes</a><br>
<a href="https://github.com/parthipanj/kissflow-xg/API-Style-Guide/wiki/API-Health-Monitoring">API Health Monitoring</a><br>
<a href="https://github.com/parthipanj/kissflow-xg/API-Style-Guide/wiki/API-Documentation">API Documentation</a></td></tr></table>
