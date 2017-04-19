Software Directory README
#########################

The Software Directory needs yearly renewal for software to not disappear from the listing on the website. To help software authors with this, scripts are provided which help you with creating a proper pull request.

The listing is split in three categories:

* **Servers** are found in the ``servers.json``,
* **Clients** are found in the ``clients.json``, and
* **Libraries** are found in the ``libraries.json``.

The tooling is the same for all three categories. What differs is what ``platforms`` means. For clients and servers, this is the list of platforms a project runs on. For libraries, this is the list of languages they support.

**Note:** You can of course also manually edit the JSON files if that’s what you prefer. Make sure to keep the diff minimal. All times are UTC.


Renewing your existing entry
============================

For renewing (and changing) an existing entry, you can use the ``update-entry.py`` tool from the command line. Example::

  ./update-entry.py clients.json Conversations

The tool will ask for confirmation::

  difference between old and new:
  --- before
  +++ after
  @@ -1,8 +1,8 @@
   {
  -    "last_renewed": null,
  +    "last_renewed": "2017-03-23T15:13:58",
       "name": "Conversations",
       "platforms": [
           "Android"
       ],
       "url": "https://github.com/siacs/Conversations"
   }
  is this okay? [y/n]

After confirmation, it writes the changes to the ``clients.json``. This works just the same for ``servers.json`` and ``libraries.json``. You can then add and commit the changes to git as usual. **Validate** that your entry is correct using the ``./lint-tool.py`` on the respective JSON file and then make a Pull Request on GitHub.


Updating information
--------------------

When asking the tool for ``--help``, you will notice that it supports a few other options too::

  usage: update-entry.py [-h] [--rename NAME] [--set-url URL]
                         [--set-platforms PLATFORM [PLATFORM ...]]
                         [--no-renewal] [--no-ask]
                         JSONFILE [NAME]

  Renew a software entry in the software list.

  positional arguments:
    JSONFILE              Software list JSON file to manipulate
    NAME                  Current name of the project

  optional arguments:
    -h, --help            show this help message and exit
    --rename NAME         Rename the project
    --set-url URL         Change the URL of the project
    --set-platforms PLATFORM [PLATFORM ...]
                          Change the contents of the last column
    --no-renewal
    --no-ask              Do not ask for confirmation before applying changes.

The following options are useful for updating information about your project:

* ``--rename``: If you need to change the name in the registry, this option is for you. It will not allow you to replace another project.
* ``--set-url``: Change the URL to which your project links.
* ``--set-platforms``: Set the words shown in the third column: if your project is a client or server, this is the list of platforms it runs on. if your project is a library, this is the language(s) it supports.

  Example use::

    ./update-entry.py clients.json Pidgin --set-platforms 'Windows' 'Linux'

  **Note:** For clients and servers, the platforms are restricted to those named in the ``platform.json`` file!

Do not set ``--no-ask`` and always be sure to review that your changes do what you intend them to do.

If you do not know how to spell your project correctly, leave out the ``NAME`` argument; the tool will list the project it knows.

Do not forget to **validate** that your entry is correct using the ``./lint-tool.py`` on the respective JSON file and then make a Pull Request on GitHub.


Add a new entry
===============

There is no tooling for that. Add the following template to the respective ``json`` file:

.. code-block:: json

      {
          "platforms": ["GNU Hurd", "Plan9"],
          "last_renewed": null,
          "name": "My Fancy New Client",
          "url": "https://myfancyclient.example"
      }

Insert it into the top-level JSON Array as last element by adding a comma after the last ``,`` and then pasting the above template with your modifications. Use the tool as described in the previous section to perform a renewal (this will sort the list correctly to minimize future diffs).

**If you do not use the tool**, make sure that you set the ``last_renewed`` key manually to the current date (as seen in other entries) in UTC and adhere to the sorting requirements of the JSON file. You can use the ``lint-list.py`` tool to verify that everything is in order. If ``lint-list.py`` complains, the Travis  CI will reject your Pull Request.

Finally, create a Pull Request.


Remove an existing entry
========================

Simply drop the corresponding JSON Object from the array and make a PR. Use the ``./lint-list.py`` tool to ensure that the syntax is still valid.


Validating Entries
==================

To validate that the list contents are okay, use the ``lint-list.py`` tool::

  ./lint-list.py clients.json

Note: The tool can only be used on the three lists and does not require an absolute path to the list.
