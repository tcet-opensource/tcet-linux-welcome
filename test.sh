#!/bin/env bash

git clone https://github.com/tcet-opensource/tcet-linux-pkgbuild.git 
cd tcet-linux-pkgbuild/apps/tcet-linux-welcome
sed -i '/^pkgrel=/s/pkgrel=.*/pkgrel=$rel/' PKGBUILD
updatedRel=$rel+1
echo "rel=$updatedRel" >> $GITHUB_ENV
cat PKGBUILD