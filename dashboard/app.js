// 월부 강의 데이터
const courses = [
    {
        name: "열반스쿨 기초반",
        fullName: "열반스쿨 기초반 - 1500만원으로 시작하는 소액 부동산 투자법",
        instructors: "너바나, 자음과모음, 주우이",
        category: "부동산 투자 기초",
        rating: 4.98,
        reviews: 172661,
        url: "https://weolbu.com/product/4644",
        note: "간판 정규 강의. 85기 이상 운영"
    },
    {
        name: "실전준비반",
        fullName: "실전준비반 - 1억 더 오를 아파트, 임장/임장보고서로 고르는 법",
        instructors: "너나위, 자음과모음, 권유디, 코크드림",
        category: "부동산 중급(수도권)",
        rating: 4.98,
        reviews: 147608,
        url: "https://weolbu.com/product/4499",
        note: "48일 / 총 16개 수업"
    },
    {
        name: "열반스쿨 중급반",
        fullName: "열반스쿨 중급반 - 직장인이 투자로 10억 달성하는 법",
        instructors: "월부멘토, 밥잘사주는부자마눌, 양파링, 잔쟈니, 주우이",
        category: "부동산 투자 중급",
        rating: 4.98,
        reviews: 106426,
        url: "https://weolbu.com/product/2492",
        note: "기수별 갱신"
    },
    {
        name: "재테크 기초반",
        fullName: "재테크 기초반 - 2026년 같은 월급 2배 더 빨리 모으는 재테크 성공공식",
        instructors: "너나위, 광화문금융러, 권유디",
        category: "재테크 기초",
        rating: 4.95,
        reviews: 50000,
        url: "https://weolbu.com/product/4818",
        note: "약 400,000원. 월급관리·주식·부동산·연금·보험 종합"
    },
    {
        name: "너나위의 저평가 아파트 찾는 법",
        fullName: "너나위의 저평가 아파트 찾는 법 (부동산 투자 원칙)",
        instructors: "너나위",
        category: "부동산 기초 > 투자 입문",
        rating: 4.96,
        reviews: 4708,
        url: "https://weolbu.com/product/4503",
        note: "시그니처 강의. BEST 태그. 28일"
    },
    {
        name: "너나위의 부동산 투자 원칙",
        fullName: "돈이 일하게 만드는 너나위의 부동산 투자 원칙 (25년 1월 개정판)",
        instructors: "너나위",
        category: "부동산 기초 / 내집마련 / 지역 분석",
        rating: 4.96,
        reviews: 4708,
        url: "https://weolbu.com/product/4135",
        note: "가치 있는 부동산을 가려내는 안목"
    },
    {
        name: "서울 부동산 소액 투자법",
        fullName: "2천만원으로 시작하는 서울 부동산 소액 투자법",
        instructors: "서쪽도사",
        category: "부동산 > 청약/재개발",
        rating: 4.94,
        reviews: 918,
        url: "https://weolbu.com/product/2734",
        note: "15년차 투자자, 순자산 50억. 4개 수업 / 3시간 30분"
    },
    {
        name: "서울 투자 기회 제대로 잡는 법",
        fullName: "서울 투자 기회 제대로 잡는 법",
        instructors: "훨훨, 플팩",
        category: "부동산 > 수도권 투자",
        rating: 4.79,
        reviews: 738,
        url: "https://weolbu.com/class/4",
        note: "서울 지도 혜택 제공, NEW/당일특가 태그"
    },
    {
        name: "투자 왕초보 경제적 자유 달성법",
        fullName: "투자 왕초보가 141만원으로 경제적 자유 달성하는 법",
        instructors: "유근용",
        category: "부동산 기초",
        rating: 4.95,
        reviews: 940,
        url: "https://weolbu.com/class/39",
        note: "BEST 태그 부착 인기 강의"
    },
    {
        name: "주우이의 청약 완성",
        fullName: "주우이의 청약 당첨부터 입주까지 한 강의로 완성",
        instructors: "주우이",
        category: "부동산 기초 > 청약",
        rating: 4.97,
        reviews: 366,
        url: "https://weolbu.com/class/39",
        note: "청약 전문 강의"
    }
];

// 강의별 상세 후기 데이터
const courseReviews = [
    {
        name: "열반스쿨 기초반",
        pros: [
            "초보자도 이해 가능한 체계적인 커리큘럼",
            "입지요소, 시세트래킹 방법, 저평가 지역 분석법 등 실질적 기법 습득",
            "강의 몰입도가 높아 긴 강의에도 집중력 유지",
            "강사의 실패 사례까지 솔직하게 공유하여 현실감 있는 학습"
        ],
        cons: [
            "수강 경쟁 치열 — \"광클\" 필요",
            "이미 지식이 있는 사람에게는 내용이 얕을 수 있음",
            "계속 들어야 할 것 같은 분위기 (락인 효과)",
            "부동산 올인 투자 권유 경향, 다른 투자 대안 시각 부족"
        ]
    },
    {
        name: "열반스쿨 중급반",
        pros: [
            "구체적 목표 설정 (10억 달성)에 도움",
            "전세레버리지, 저평가 아파트 선별 등 실전 내용",
            "투자자 생활 태도(독서·가족·공부 균형) 인사이트 제공"
        ],
        cons: [
            "전세레버리지 리스크에 대한 두려움",
            "저평가 기준과 전세 안정성 동시 고려의 어려움",
            "기초반과 일부 내용 중복"
        ]
    },
    {
        name: "내집마련 기초반 (내마기)",
        pros: [
            "내집마련 성공 사례 다수 (5천만원 네고 등)",
            "수도권/지방 기준 차이를 명확히 설명",
            "조모임(스터디) 시스템으로 동기 부여 효과 우수",
            "튜터와 동기들의 친절한 질의응답 지원"
        ],
        cons: [
            "강의 가격 부담 (약 45~50만원, 부부 시 월 90만원)",
            "조모임 종료 후 톡방 삭제로 네트워킹 단절",
            "심화 학습을 위해 추가 강의 수강 필요"
        ]
    },
    {
        name: "실전준비반",
        pros: [
            "실전 임장 및 임장보고서 작성 노하우 직접 학습",
            "4개월 만에 투자 성공 사례 존재 (용인 수지구 등)",
            "기초반에서 자연스럽게 연결되는 단계적 커리큘럼"
        ],
        cons: [
            "임보 작성 강조 — 수강생 데이터를 플랫폼이 활용한다는 의구심",
            "\"공부를 위한 공부\"에 머물 수 있다는 비판",
            "수강 경쟁 과열로 접근성 낮음"
        ]
    },
    {
        name: "지방투자 기초반 / 실전반",
        pros: [
            "소액으로도 투자 시작 가능한 A to Z 안내",
            "광역시 초신축 아파트 매수 등 실제 성공 사례",
            "지방 도시별 선호요소·생활권 분석 방법 구체적 제공",
            "수도권 투자 종잣돈 마련 전략으로 활용 가능"
        ],
        cons: [
            "지방 부동산 시장 변동성이 큼 — 리스크 경고 부족",
            "특정 지역 편중 분석 우려"
        ]
    }
];

// 테이블 렌더링
function renderTable(data) {
    const tbody = document.getElementById("courseBody");
    tbody.innerHTML = data.map(c => `
        <tr>
            <td>
                <strong>${c.name}</strong>
                <br><small style="color: var(--text-light)">${c.note}</small>
            </td>
            <td>${c.instructors}</td>
            <td>${c.category}</td>
            <td><span class="rating-badge">⭐ ${c.rating.toFixed(2)}</span></td>
            <td>${c.reviews.toLocaleString()}</td>
            <td><a href="${c.url}" target="_blank" class="link-btn">바로가기</a></td>
        </tr>
    `).join("");
}

// 검색 및 정렬
function filterAndSort() {
    const query = document.getElementById("searchInput").value.toLowerCase();
    const sortBy = document.getElementById("sortSelect").value;

    let filtered = courses.filter(c =>
        c.name.toLowerCase().includes(query) ||
        c.fullName.toLowerCase().includes(query) ||
        c.instructors.toLowerCase().includes(query)
    );

    filtered.sort((a, b) => {
        if (sortBy === "rating") return b.rating - a.rating;
        if (sortBy === "reviews") return b.reviews - a.reviews;
        return a.name.localeCompare(b.name, "ko");
    });

    renderTable(filtered);
}

// 아코디언 렌더링
function renderAccordion() {
    const container = document.getElementById("reviewAccordion");
    container.innerHTML = courseReviews.map((r, i) => `
        <div class="accordion-item" data-index="${i}">
            <button class="accordion-header" onclick="toggleAccordion(${i})">
                <span>${r.name}</span>
                <span class="accordion-arrow">▼</span>
            </button>
            <div class="accordion-body">
                <div class="accordion-content">
                    <h4 class="pro">✅ 긍정적 후기</h4>
                    <ul>${r.pros.map(p => `<li>${p}</li>`).join("")}</ul>
                    <h4 class="con">❌ 비판적 후기</h4>
                    <ul>${r.cons.map(c => `<li>${c}</li>`).join("")}</ul>
                </div>
            </div>
        </div>
    `).join("");
}

function toggleAccordion(index) {
    const item = document.querySelector(`.accordion-item[data-index="${index}"]`);
    item.classList.toggle("active");
}

// 차트 렌더링
function renderCharts() {
    const labels = courses.map(c => c.name);
    const reviewCounts = courses.map(c => c.reviews);
    const ratings = courses.map(c => c.rating);

    const colors = [
        "#2563eb", "#7c3aed", "#059669", "#d97706", "#dc2626",
        "#0891b2", "#4f46e5", "#c026d3", "#65a30d", "#ea580c"
    ];

    // 후기 수 차트
    const reviewsCtx = document.getElementById("reviewsChart").getContext("2d");
    new Chart(reviewsCtx, {
        type: "bar",
        data: {
            labels: labels,
            datasets: [{
                label: "후기 수",
                data: reviewCounts,
                backgroundColor: colors.map(c => c + "cc"),
                borderColor: colors,
                borderWidth: 1,
                borderRadius: 6
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: false },
                tooltip: {
                    callbacks: {
                        label: ctx => `후기: ${ctx.raw.toLocaleString()}개`
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: v => v >= 1000 ? (v / 1000) + "K" : v
                    }
                },
                x: {
                    ticks: {
                        maxRotation: 45,
                        font: { size: 11 }
                    }
                }
            }
        }
    });

    // 평점 차트
    const ratingsCtx = document.getElementById("ratingsChart").getContext("2d");
    new Chart(ratingsCtx, {
        type: "bar",
        data: {
            labels: labels,
            datasets: [{
                label: "평점",
                data: ratings,
                backgroundColor: ratings.map(r =>
                    r >= 4.97 ? "#16a34acc" :
                    r >= 4.95 ? "#2563ebcc" :
                    r >= 4.90 ? "#d97706cc" : "#64748bcc"
                ),
                borderColor: ratings.map(r =>
                    r >= 4.97 ? "#16a34a" :
                    r >= 4.95 ? "#2563eb" :
                    r >= 4.90 ? "#d97706" : "#64748b"
                ),
                borderWidth: 1,
                borderRadius: 6
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: false },
                tooltip: {
                    callbacks: {
                        label: ctx => `평점: ${ctx.raw.toFixed(2)}`
                    }
                }
            },
            scales: {
                y: {
                    min: 4.7,
                    max: 5.0,
                    ticks: {
                        stepSize: 0.05,
                        callback: v => v.toFixed(2)
                    }
                },
                x: {
                    ticks: {
                        maxRotation: 45,
                        font: { size: 11 }
                    }
                }
            }
        }
    });
}

// 초기화
document.addEventListener("DOMContentLoaded", () => {
    renderTable(courses);
    renderAccordion();
    renderCharts();

    document.getElementById("searchInput").addEventListener("input", filterAndSort);
    document.getElementById("sortSelect").addEventListener("change", filterAndSort);
});
