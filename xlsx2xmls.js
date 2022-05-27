// https://github.com/cujarrett/markdown-tables

import fs from "fs"
import xlsx from "xlsx"

export const getInput = async (filePath, sheetNumber = 0) => {
  const workbook = xlsx.readFile(filePath, { sheetStubs: true })
  const sheetNames = workbook.SheetNames
  const input = workbook.Sheets[sheetNames[sheetNumber]]
  return xlsx.utils.sheet_to_json(input, { defval: "" })
}

export const getColumns = (data) => {
  let headers = []
  const columns = []
  let maxRowLength = 0

  for (const rowItems of data) {
    if (Object.keys(rowItems).length > maxRowLength) {
      headers = [...Object.keys(rowItems)]
      maxRowLength = Object.keys(rowItems).length
    }
  }

  for (const header of headers) {
    const column = [header]
    for (const row of data) {
      const value = row[header] || ""
      column.push(value)
    }
    columns.push(column)
  }

  return columns
}

export const xmlDir = async (input, outputPath) => {
  try {
    const table = await getInput(input)
    const columns = getColumns(table)

    if (!fs.existsSync(outputPath)) {
      fs.mkdirSync(outputPath)
    }

    for (let rowIndex = 2; rowIndex < 7; rowIndex++) {
      let output = "<resources>\n"
      for (let columnIndex = 1; columnIndex < columns[rowIndex].length; columnIndex++) {

        let element = columns[rowIndex][columnIndex] || ""
        element = element.toString().replace(/&/g, "&amp;")

        if (element !== "") {
          output += '  <string name="' + columns[1][columnIndex] + '" platform="' + columns[0][columnIndex] + '">' + element + '</string>\n'
        }
      }
      output += '</resources>\n'
      fs.writeFileSync(outputPath + "/" + columns[rowIndex][0] + ".xml", output)
    }

  } catch (error) {
    // eslint-disable-next-line no-console
    console.log(error)
    throw error
  }
}

xmlDir("./client.xlsx", "./client")
