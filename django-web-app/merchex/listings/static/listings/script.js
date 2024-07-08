'use strict';
/* eslint-env browser */

document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('.header-container');

  // Suppression de l'écouteur d'événement de scroll pour le header
});

const fermerMenu = () => {
  // Récupérer le menu
  const input = document.getElementById('menu-cb');
  input.checked = false;

  const fenetreNode = document.getElementById('menu-cote');
  if (fenetreNode) {
    fenetreNode.remove();
  }
}

const changerEtatMenu = () => {
  // Récupérer le menu
  const input = document.getElementById('menu-cb');
  const actif = input.checked;

  if (actif) {
    const fenetreNode = document.createElement('div');
    fenetreNode.id = 'menu-cote';
    fenetreNode.className = 'menu-cote';
    fenetreNode.addEventListener('click', fermerMenu);
    document.body.appendChild(fenetreNode);
  } else {
    const fenetreNode = document.getElementById('menu-cote');
    if (fenetreNode) {
      fenetreNode.remove();
    }
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const input = document.getElementById('menu-cb');
  if (input) {
    input.addEventListener('click', changerEtatMenu);
  }
});