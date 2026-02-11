# Software Directory README

To help software authors maintain their software entries, scripts are provided which help you with creating a proper pull request.

All software entries are contained in `data/software.json`. You can either edit this file [directly via GitHub](https://github.com/xsf/xmpp.org/edit/master/data/software.json) or use the tool provided.

- [Modifying your existing entry](#modifying-your-existing-entry)
- [Add a new entry](#add-a-new-entry)
- [Remove an existing entry](#remove-an-existing-entry)
- [Validating Entries](#validating-entries)

Please note that if you provide a DOAP file url, both "platforms" and "url" keys must be empty, as they are sourced from the DOAP file. Example:

```json
{
  "categories": [
    "client"
  ],
  "doap": "https://example.org/file.doap",
  "name": "App Name",
  "platforms": [],
  "url": null
}
```

A note on the `platforms` key: For clients and servers, this is the list of platforms a project runs on. For libraries, this is the list of languages they support.

## Modifying your existing entry

For changing an existing entry, you can use the `update_entry.py` tool from the command line. Example:

```shell
./update_entry.py Conversations
```

The tool will ask for confirmation:

```diff
  difference between old and new:
  --- before
  +++ after
  @@ -1,8 +1,8 @@
   {
  -    "doap": null,
  +    "doap"; "https://raw.githubusercontent.com/iNPUTmice/Conversations/master/conversations.doap",
       "name": "Conversations",
       "platforms": [],
       "url": null,
       "categories": [
           "client"
       ]
   }
  is this okay? [y/n]
```

After confirmation, it writes the changes to `data/software.json`. You can then add and commit the changes to git as usual. **Validate** that your entry is correct using `./lint_software_list.py` and then make a Pull Request on GitHub.

## Updating information

When asking the tool for `--help`, you will notice that it supports a few other options too:

```shell
  usage: update_entry.py [-h] [--rename NAME] [--set-url URL] [--set-doap URL]
                         [--set-platforms PLATFORM [PLATFORM ...]]
                         [--no-ask]
                         [NAME]

  Modify a software entry in the software list.

  positional arguments:
    NAME                  Current name of the project

  optional arguments:
    -h, --help            show this help message and exit
    --rename NAME         Rename the project
    --set-url URL         Change the URL of the project
    --set-doap URL        Change the URL of the project DOAP file
    --set-platforms PLATFORM [PLATFORM ...]
                          Change the contents of the last column
    --no-ask              Do not ask for confirmation before applying changes.
```

The following options are useful for updating information about your project:

* `--rename`: If you need to change the name in the registry, this option is for you. It will not allow you to replace another project.
* `--set-url`: Change the URL to which your project links.
* `--set-platforms`: Set the words shown in the third column: if your project is a client or server, this is the list of platforms it runs on. if your project is a library, this is the language(s) it supports.

Example use:

```shell
./update_entry.py Pidgin --set-platforms 'Windows' 'Linux'
```

Do not set `--no-ask` and always be sure to review that your changes do what you intend them to do.

If you do not know how to spell your project correctly, leave out the `NAME` argument; the tool will list the project it knows.

Do not forget to **validate** that your entry is correct using the `./lint_software_list.py` and then make a Pull Request on GitHub.

## Add a new entry

There is no tooling for that. Add the following template to `data/software.json`:

```json
{
    "name": "My Fancy New Client",
    "doap": "https://myfancyclient.example/doap.rdf",
    "platforms": [],
    "url": null,
    "categories": [
      "client"
    ]
}
```

Insert it into the top-level JSON Array as last element by adding a comma after the last `,` and then pasting the above template with your modifications. Use the tool as described in the previous section to perform a modification (this will sort the list correctly to minimize future diffs).

**If you do not use the tool**, make sure that you adhere to the sorting requirements of the JSON file. You can use the `lint_software_list.py` tool to verify that everything is in order. If `lint_software_list.py` complains, the CI will reject your Pull Request.

Finally, create a Pull Request.

**Note**: The JSON file must be saved using UTF-8 character encoding, without a Byte Order Mark (BOM). Using other character encodings, or including a BOM may result in the failure of the validation procedure, which will cause the pull request to be rejected.

## Remove an existing entry

Simply drop the corresponding JSON Object from the array and make a PR. Use the `./lint_software_list.py` tool to ensure that the syntax is still valid.

## Validating Entries

To validate that the list contents are okay, use the `./lint_software_list.py` tool:

```shell
./lint_software_list.py software.json
```
