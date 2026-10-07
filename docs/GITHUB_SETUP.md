# Publish the starter project

This archive contains a prepared folder, not an already published GitHub repository.

1. Extract `Open-Source-Kana-GitHub-Starter.zip`.
2. Review the files and complete the audio/content checks listed in `REVIEW_STATUS.md`.
3. Create a public GitHub repository named `open-source-kana`. Leave the automatic license selection blank because this project already supplies scoped license notices.
4. Use GitHub Desktop to add the extracted `open-source-kana` folder as a local repository. If it is not yet a Git repository, use the offered option to create one there. Check that you selected the project folder containing README.md, not its parent.
5. Commit the files. Publish to your GitHub account, or connect this local repository to the repository created in step 3.
6. Create a release tagged `v1.0.0`. Attach the two packages in `releases/v1.0.0/`, and optionally the PowerPoints in `workbooks/`.
7. Add the repository and release URLs to README.md. Enable Issues as the feedback channel and add a link to it in future deck descriptions.

You can also use git from the extracted project directory:

```sh
git init
git add .
git commit -m "Add Hiragana and Katakana workbooks and Anki decks"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the URL copied from your own empty repository. These commands assume git is installed and authentication is already set up. If the remote already has commits, use GitHub Desktop to clone it first and copy the project files into that clone.

For future releases, update editable data/templates, rebuild, test, and publish a new version. Preserve note GUIDs when correcting existing cards. Avoid committing generated `dist/` files; put new download packages in Releases.
