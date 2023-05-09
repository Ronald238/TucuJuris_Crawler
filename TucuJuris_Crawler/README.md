<h2>TucuJuris Crawler <img src="https://cdn.edu.buncee.com/assets/abbde3e5bc174eb59c55d4b2f278ec48/animation-library-magicbookp-022120.gif?timestamp=1582320629" width="60"></h2>

  
*This Python code is a class called "ConsultaProcessual" that inherits from the class "Tucujuris". The "Tucujuris" class contains a method to perform HTTP requests ("request" method), a method to initialize and close sessions ("__enter__" and "__exit__" methods, respectively) and a "start" method that receives a field dictionary and returns data extracted from each HTTP request response. The "ConsultaProcessual" class defines two functions that perform the extraction of data from legal proceedings of Brazilian courts.*

*The "buscar_links" function is used to perform a GET request to a public API of the court specified in the "self.Tribunal" attribute. The function searches for process details based on a dictionary of fields provided by the user. Then the return of the GET request is parsed and the links for each process are extracted and stored in a list for later use.*

*The "extract_data" function is used to extract the relevant data for each process from the links retrieved in the "search_links" function. The function sends a GET request to the public API with the link to the process, extracts the relevant information (like header, involved parties, process movement, etc.) and returns a dictionary with that data.*

*Both functions call the "request" method to perform HTTP requests, which uses the Python "requests" library to send HTTP requests based on the provided arguments (method type, URL, parameters, data, headers, and timeout). The arguments for the "request" method are passed as parameters to the "search_links" and "extract_data" functions.*

*The code also imports other Python libraries (such as "os", "json", "logging" and "datetime") and a custom class called "Base". The code also uses the "__init__" and "__exit__" initialization methods and the "self" attributes to define and access variables internal to the class. The "ConsultaProcessual" class is used to access data from a specific judicial court in Brazil and extract information from court cases.*
<div>

<h2>Technologies used <img src="https://media.tenor.com/o2NcvHhvH8wAAAAi/pixelbot-robot.gif" width="50"></h2>
<div>
  <img align="center" height="50" weight="60" img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" />
  <img align="center" height="50" weight="60" img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" />
  <img align="center" height="50" weight="60" img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original-wordmark.svg" />

<h2>Libraries used/links<img src="https://media.tenor.com/wOar0JtSmEcAAAAi/link-zelda.gif" width="50"></h2>
<div>
<a href="https://tucujuris.tjap.jus.br/tucujuris/pages/consultar-processo/consultar-processo.html"/>
◦Tucujuris: This was the site used for this code.
</a>

<div>
<a href="https://docs.python.org/3/library/time.html"/>
◦Librarie time: This module provides various time-related functions.
</a>

<div>
<a href="https://docs.python.org/3/library/os.html">
◦Librarie os: his module provides a portable way of using operating system dependent functionality. 
</a>

<div>
<a href="https://pypi.org/project/requests/">
◦Librarie requests: Requests allows you to send HTTP/1.1 requests extremely easily.
</a>

<div>
<a href="https://docs.python.org/3/library/json.html">
◦Librarie json: Json exposes an API familiar to users of the standard library marshal and pickle modules.
</a>

<div>
<a href="https://docs.python.org/3/library/logging.html">
◦Librarie logging: This module defines functions and classes which implement a flexible event logging system for applications and libraries.
</a>

<div>
<a href="https://docs.python.org/3/library/datetime.html">
◦Librarie datetime: he datetime module supplies classes for manipulating dates and times.
</a>


