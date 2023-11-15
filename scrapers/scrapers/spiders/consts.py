ACTION_CLASSIFIERS = (
    ("Approved by the Governor", ["executive-signature"]),
    ("Bill read. Veto not sustained", ["veto-override-passage"]),
    ("Bill read. Veto sustained", ["veto-override-failure"]),
    ("Enrolled and delivered to Governor", ["executive-receipt"]),
    ("From committee: .+? adopted", ["committee-passage"]),
    # the committee and chamber passage can be combined, see NV 80 SB 506
    (
        r"From committee: .+? pass(.*)Read Third time\.\s*Passed\.",
        ["committee-passage", "reading-3", "passage"],
    ),
    ("From committee: .+? pass", ["committee-passage"]),
    ("Prefiled. Referred", ["introduction", "referral-committee"]),
    ("Read first time. Referred", ["reading-1", "referral-committee"]),
    ("Read first time.", ["reading-1"]),
    ("Read second time.", ["reading-2"]),
    ("Read third time. Lost", ["failure", "reading-3"]),
    ("Read third time. Passed", ["passage", "reading-3"]),
    ("Read third time.", ["reading-3"]),
    ("Rereferred", ["referral-committee"]),
    ("Resolution read and adopted", ["passage"]),
    ("Enrolled and delivered", ["enrolled"]),
    ("To enrollment", ["passage"]),
    ("Approved by the Governor", ["executive-signature"]),
    ("Vetoed by the Governor", ["executive-veto"]),
)

session_slugs = {
    "2010Special26": "26th2010Special",
    "2013Special27": "27th2013Special",
    "2014Special28": "28th2014Special",
    "2015Special29": "29th2015Special",
    "2016Special30": "30th2016Special",
    "2020Special31": "31st2020Special",
    "2020Special32": "32nd2020Special",
    "2021Special33": "33rd2021Special",
    "2023Special34": "34th2023Special",
    "2023Special35": "35th2023Special",
    "75": "75th2009",
    "76": "76th2011",
    "77": "77th2013",
    "78": "78th2015",
    "79": "79th2017",
    "80": "80th2019",
    "81": "81st2021",
    "82": "82nd2023",
}

# NV sometimes carries-over bills from previous sessions,
# without regard for bill number conflicts.
# so AB1* could get carried in, even if there's already an existing AB1
# The number of asterisks represent which past session it was pulled in from,
# which can include specials, and skip around, so this can't be automated.
# The list is at https://www.leg.state.nv.us/Session/81st2021/Reports/BillsListLegacy.cfm?DoctypeID=1
# where 81st2021 will need to be swapped in for the session code.
CARRYOVERS = {
    "80": {
        "*": "2017",
    },
    "81": {
        "*": "2019",
        "**": "2020Special32",
    },
    "82": {"*": "2021"},
}
