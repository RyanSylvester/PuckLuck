import React from 'react'

export default function index(
  standingsJSON
) {
  const standings = (standingsJSON.standingsJSON);
  const standing_values = standings.map((key) => 
    <div>{key.Team} finished with {key.P} points.</div>
  );
  return (
    <div>
      <div><b>STANDINGS</b></div>
      <div>{standing_values}</div>
    </div>
  )
}
