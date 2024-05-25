import React from 'react';
import Modal from 'react-modal';
import './ContactDetail.css';

Modal.setAppElement('#root');

const ContactDetail = ({ isOpen, onRequestClose, contact }) => {
  if (!contact) return null;

  return (
    <Modal
      isOpen={isOpen}
      onRequestClose={onRequestClose}
      contentLabel="Contact Details"
      className="Modal"
      overlayClassName="Overlay"
    >
      <h2>{contact.name}</h2>
      <p><strong>Username:</strong> {contact.username}</p>
      <p><strong>Email:</strong> {contact.email}</p>
      <p><strong>Phone:</strong> {contact.phone}</p>
      <p><strong>Website:</strong> <a href={`http://${contact.website}`} target="_blank" rel="noopener noreferrer">{contact.website}</a></p>
      <p><strong>Address:</strong> {contact.address.street}, {contact.address.suite}, {contact.address.city}, {contact.address.zipcode}</p>
      <p><strong>Company:</strong> {contact.company.name}</p>
      <button onClick={onRequestClose} className="close-button">Close</button>
    </Modal>
  );
};

export default ContactDetail;
