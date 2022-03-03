const copyToClipboard = (text) => {
    let aux = document.createElement("input");
    aux.setAttribute("value", text);
    document.body.appendChild(aux);
    aux.select();
    document.execCommand("copy");
    document.body.removeChild(aux);
};


const tableSort = (index) => {
    let table, rows, i;
    table = document.getElementById('this-table');

    let switchButton = document.getElementById('this-table-sort-' + index);

    let buttonType = switchButton.className;
    // Change icon
    if (buttonType === 'fa fa-sort' || buttonType === 'fa fa-sort-desc') {
        switchButton.className = 'fa fa-sort-asc';
    } else {
        switchButton.className = 'fa fa-sort-desc';
    }

    // Switch back to unfold more for all other types
    let indices = [0, 1, 2, 3];
    for (let i = 0; i < indices.length; i++) {
        if (indices[i] !== index) {
            let switchButtonOther = document.getElementById('this-table-sort-' + indices[i]);
            switchButtonOther.className = 'fa fa-sort';
        }
    }

    // Helper for inserting rows before. Non-pure.
    function insertBefore(collection, leftIndex, rightIndex) {
      collection[leftIndex].parentNode.insertBefore(collection[leftIndex], collection[rightIndex]);
    }

    // Helper for retrieving TD nodes
    const getTDNode = (row) => {
      return row.getElementsByTagName("TD")[index];
    };

    // Short-hand Strategy design-pattern for comparing elements
    const compareMax = (left, right) => left > right ? -1 : 1;
    const compareMin = (left, right) => left <= right ? -1 : 1;
    const sortStrategy = buttonType === 'fa fa-sort' || buttonType === 'fa fa-sort-desc'
      ? compareMin : compareMax;

    // Short-hand Strategy design-pattern for retrieving values from rows
    const getDescendantValue = (row) => getTDNode(row).innerHTML.toLowerCase();

    const getDateValue = (row) => {
      let str = getTDNode(row).innerHTML.toLowerCase().replace(/\s/g, '');
      if (str) {
        return new Date(getTDNode(row).innerHTML.toLowerCase())
      } else {
        return new Date('12-31-20 05:05')
      }
    };

    const getIntValue = (row) => {
        const vInt = parseInt(getDescendantValue(row));
        if (!vInt) {
            return 100000000
        }
        return vInt
    }

    const getValueStrategy = (v) => {
      if ([0, 2].includes(index)) {
          return getDescendantValue(v)
      } else if (index === 1) {
          return getDateValue(v)
      } else {
          return getIntValue(v)
      }
    };

    rows = table.rows;

    for (i = 1; i < (rows.length - 1); i++) {
      const leftIndex = i;
      let rightIndex = i;
      for (let j = i; j < rows.length; j++) {
        rightIndex = sortStrategy(getValueStrategy(rows[rightIndex]), getValueStrategy(rows[j])) > 0
          ? j
          : rightIndex;
      }

      insertBefore(rows, rightIndex, leftIndex);

    }
}


const mockDataGrab = () => {
    const button = document.getElementById('mock-data-grab-btn');
    button.disabled = true;

    // Get form
    const item = document.getElementById('selectItem').value;

    $(".data-area").empty();

    $.ajax({
      url: `/mock-data-grab/send`,
      data: {
          "item": item
      },
      method: "POST",
      success: function(response) {
        $(".data-area").append(response);
        $("#mock-data-grab-btn").prop( "disabled", false );
      },
      error: function(error) {
      }
    });
}